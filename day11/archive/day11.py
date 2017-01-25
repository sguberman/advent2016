from collections import defaultdict
from itertools import combinations, chain
import logging
logging.basicConfig(level=logging.WARNING)


def a_star(start, goal):
    """
    A* search algorithm from pseudocode at Wikipedia:
    https://en.wikipedia.org/wiki/A*_search_algorithm
    """
    # the set of nodes already evaluated (starts empty)
    closed_set = set()

    # the set of currently discovered nodes that are not already evaluated
    # initially only the start node is known
    open_set = set()
    open_set.add(start)

    # for each node, which node it can most efficiently be reached from
    # if a node can be reached from many nodes, came_from will eventually
    # contain the most efficient previous step
    came_from = {}

    # for each node, the cost of getting from the start node to that node
    # the cost of going from start to start is zero
    g_score = defaultdict(lambda: 99999)
    g_score[start] = 0

    # for each node, the total cost of getting from the start node to the goal
    # by passing that node (partly known, partly heuristic)
    # completely heuristic for start node
    f_score = defaultdict(lambda: 99999)
    f_score[start] = heuristic_cost_estimate(start, goal)

    while open_set:
        log = f'os: {len(open_set)}\tcs: {len(closed_set)}\t'
        logging.info(log)
        current = min(open_set, key=lambda x: f_score[x])
        logging.debug(f'open_set loop current: {current}')

        if current == goal:
            return reconstruct_path(came_from, current)

        open_set.remove(current)
        closed_set.add(current)

        for neighbor in neighbors(current, goal):
            if neighbor in closed_set:  # ignore already evaluated
                continue

            tentative_g_score = (g_score[current] +
                                 dist_between(current, neighbor))

            if neighbor not in open_set:  # discover a new node
                open_set.add(neighbor)
            elif tentative_g_score >= g_score[neighbor]:
                continue  # this is not a better path

            # this is the best path yet, record it!
            came_from[neighbor] = current
            g_score[neighbor] = tentative_g_score
            f_score[neighbor] = (g_score[neighbor] +
                                 heuristic_cost_estimate(neighbor, goal))

    return False  # no solution


def reconstruct_path(came_from, current):
    """
    From the same Wikipedia A* article.
    """
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    return total_path


def heuristic_cost_estimate(node, goal):
    """
    AKA "Distance to goal," should not overestimate actual cost.
    In this case, I will guess based on the number of floors between each
    component and its final floor. When all components are on the right floor,
    then the estimate will be zero.
    """
    # this part could be optimized out if we only ever
    # want to move everything to the fourth floor
    goal_locations = {}
    for i, floor in enumerate(goal):
        for item in floor:
            goal_locations[item] = i

    distances = {}
    for j, floor in enumerate(node):
        for item in floor:
            distances[item] = abs(goal_locations[item] - j)

    return sum(dist / 6 for dist in distances.values())


def dist_between(node1, node2):
    """
    In this case, we are only ever comparing the distance between neighboring
    nodes which is always 1.
    """
    return 1


def neighbors(node, goal):
    """
    Come up with all the possible next moves based on current status.

    Some rules from the puzzle:
        - Elevator moves one floor at a time
        - Elevator can't move without at least one component inside
        - Can't leave a microchip on a floor with another generator,
          (unless it is with its own generator too)
    """
    contents, other_floors = node.status()
    nodes = []
    for floor in other_floors:
        for payload in possible_payloads(contents):
            new_floor = tuple(sorted(('E',) + floor + payload))
            leftover_floor = tuple(sorted(set(contents) - set(payload)))
            if is_safe(new_floor) and is_safe(leftover_floor):
                below_floors = node[:node.index(floor)]
                below_floors = clear_floors(below_floors, new_floor)
                above_floors = node[node.index(floor) + 1:]
                above_floors = clear_floors(above_floors, new_floor)
                nodes.append(Node(below_floors + (new_floor,) + above_floors))
    return sorted(nodes, key=lambda x: heuristic_cost_estimate(x, goal))


def is_safe(floor):
    """
    A floor is safe if:
        - microchips are not left alone with other generators
    """
    microchips = set([item[1:] for item in floor if item.startswith('m')])
    generators = set([item[1:] for item in floor if item.startswith('g')])
    if generators and (microchips - generators):
        return False
    else:
        return True


def possible_payloads(available_items):
    for item in available_items:
        yield (item,)
    for combo in combinations(available_items, 2):
        yield combo


def clear_floors(floors, items):
    return tuple(tuple(sorted(set(floor) - {'E'} - set(items))) for floor in floors)


class Node(tuple):
    """
    This is just a tuple with a special way to instantiate.
    Pass in a series of strings, get back a tuple of sorted tuples.
    """
    @classmethod
    def fromfloors(cls, *floors):
        """
        Create a Node object from a series of strings describing each floor.

        >>> Node.fromfloors('E mH mLi', 'gH', 'gLi', '')
        (('E', 'mH', 'mLi'), ('gH',), ('gLi',), ())

        This describes 4 floors with the Elevator, Hydrogen microchip,
        and Lithium microchip on the first floor; a Hydrogen generator on the
        second floor; a Lithium generator on the third floor; nothing on the
        fourth floor.
        """
        return cls(tuple(sorted(floor.split())) for floor in floors)

    def __repr__(self):
        return '\n'.join(': '+' '.join(floor) for floor in reversed(self))

    def status(self):
        """
        Get the contents of the current floor and that of the floors
        immediately above and below.
        """
        other_floors = []
        for floor_num, items in enumerate(self):
            if 'E' in items:  # find the elevator
                contents = tuple(sorted(tuple(set(items) - {'E'})))
                if floor_num < (len(self) - 1):
                    other_floors.append(self[floor_num + 1])
                if floor_num > 0:
                    other_floors.append(self[floor_num - 1])
                return contents, other_floors

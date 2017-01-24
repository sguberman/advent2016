from collections import defaultdict
from itertools import combinations


def a_star(start, goal):
    """
    A* search algorithm from pseudocode at Wikipedia:
    https://en.wikipedia.org/wiki/A*_search_algorithm
    """
    # the set of nodes already evaluated (starts empty)
    closed_set = set()

    # the set of currently discovered nodes that are not already evaluated
    # initially only the start node is known
    open_set = {start}

    # for each node, which node it can most efficiently be reached from
    # if a node can be reached from many nodes, came_from will eventually
    # contain the most efficient previous step
    came_from = {}

    # for each node, the cost of getting from the start node to that node
    # the cost of going from start to start is zero
    g_score = defaultdict(lambda: 9999)
    g_score[start] = 0

    # for each node, the total cost of getting from the start node to the goal
    # by passing that node (partly known, partly heuristic)
    # completely heuristic for start node
    f_score = defaultdict(lambda: 9999)
    f_score[start] = heuristic_cost_estimate(start, goal)

    while open_set:
        current = min(open_set, key=lambda x: f_score[x])
        print(current)

        if current == goal:
            return reconstruct_path(came_from, current)

        open_set.remove(current)
        closed_set.add(current)

        for neighbor in neighbors(current):
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
            distances[item] = goal_locations[item] - j

    return sum(dist**2 for dist in distances.values())


def dist_between(node1, node2):
    """
    In this case, we are only ever comparing the distance between neighboring
    nodes which is always 1.
    """
    return 1


def neighbors(node):
    """
    Come up with all the possible next moves based on current status.

    Some rules from the puzzle:
        - Elevator moves one floor at a time
        - Elevator can't move without at least one component inside
        - Can't leave a microchip on a floor with another generator,
          (unless it is with its own generator too)
    """
    current_floor_num = 0  # which floor are we on?
    available_items = []
    for i, floor in enumerate(node):
        if 'E' in floor:  # find the elevator
            current_floor_num = i
            available_items = set(floor)  # what's here?
            break

    available_floors = []  # can we move up, down, or both?
    if current_floor_num < (len(node) - 1):
        available_floors.append(current_floor_num + 1)
    if current_floor_num > 0:
        available_floors.append(current_floor_num - 1)

    for floor in available_floors:
        for payload in (available_items + combinations(available_items, 2)):
            tentative_floor = ('E',) + node[floor] + payload
            previous_floor = set(available_items) - set(payload)
            if is_safe(tentative_floor) and is_safe(previous_floor):
                try:
                    yield Node(node[:floor] + tentative_floor + node[floor + 1:])
                except IndexError:
                    yield Node(node[:floor] + tentative_floor)


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


class Node(tuple):
    """
    I needed a tuple of tuples that doesn't care about order within the
    nested tuples, but does care about the order of the first-level tuples.
    That way, when checking for equivalence with the goal condition the order
    of the items on each floor doesn't matter, but the order of the floors
    themselves does matter. Can't use a set for each floor because sets are
    not hashable, thus can't be used in sets or dictionaries.

    There might be a better way to do this, but it was fun to learn about
    inheritance and overriding the equivalence and hashing operations.
    """
    def __eq__(self, other):
        """
        Order of items on each floor shouldn't matter, but floor order should.
        """
        return all(set(a) == set(b) for a, b in zip(self, other))

    def __hash__(self):
        """
        Sort the items on each floor for hash stability. Perhaps it would
        just be better to sort each floor during instantiation and leave hash
        alone.
        """
        return hash(tuple(sorted(item)) for item in self)

    @classmethod
    def fromfloors(cls, *floors):
        """
        Create a Node object from a list of strings describing each floor.

        >>> Node.fromfloors('E mH mLi', 'gH', 'gLi', '')
        (('E', 'mH', 'mLi'), ('gH',), ('gLi',), ())

        This describes 4 floors with the Elevator, Hydrogen microchip,
        and Lithium microchip on the first floor; a Hydrogen generator on the
        second floor; a Lithium generator on the third floor; nothing on the
        fourth floor.
        """
        return cls(tuple(floor.split()) for floor in floors)


if __name__ == '__main__':
    start = Node.fromfloors('E gPr mPr',
                            'gCo gCu gRu gPu',
                            'mCo mCu mRu mPu',
                            '')

    goal = Node.fromfloors('',
                           ''
                           ''
                           'E gPr mPr gCo mCo gCu mCu gRu mRu gPu mPu')

    path = a_star(start, goal)
    print(len(path))

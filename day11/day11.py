import heapq
import logging
from collections import namedtuple
from itertools import combinations, product


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def __len__(self):
        return len(self.elements)

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]


class Search:
    @staticmethod
    def a_star(start, goal):
        frontier = PriorityQueue()
        frontier.put(start, 0)
        came_from = {start: None}
        cost_so_far = {start: 0}

        while not frontier.empty():
            logging.debug(f'f: {len(frontier)} cf: {len(came_from)} '
                          f'csf: {len(cost_so_far)}')
            current = frontier.get()

            if current == goal:
                logging.debug('breaking for goal')
                break

            for new in current.neighbors():
                new_cost = cost_so_far[current] + current.cost(new)
                if new not in cost_so_far or new_cost < cost_so_far[new]:
                    cost_so_far[new] = new_cost
                    priority = new_cost + __class__.heuristic(new, goal)
                    frontier.put(new, priority)
                    came_from[new] = current

        logging.debug(f'frontier: {frontier.elements}')
        return came_from, cost_so_far

    @staticmethod
    def reconstruct_path(came_from, start, goal):
        current = goal
        path = [current]
        while current != start:
            current = came_from[current]
            path.append(current)
        path.reverse()
        return path

    @staticmethod
    def heuristic(point, goal):
        """
        Estimate the number of moves required to the goal.
        For shortest path, this cannot overestimate the actual distance.
        Use the distance between each component and the goal,
        but divide by 2 because the elevator can carry up to 2 items.
        """
        p_state = point.to_state()
        g_state = goal.to_state()
        return sum(abs(p - g) for p, g in zip(p_state, g_state)) / 4


class Point(namedtuple('Point', 'elevator microchips generators')):
    """
    This is how a node in the graph is represented.
    Each integer denotes floors for each type of component.
    The microchips and generators are in the same order.

    ex: start = Point(elevator=0, microchips=(0, 0), generators=(1, 2))
    This describes the start condition for the example puzzle.
    """
    @classmethod
    def from_state(cls, state):
        """
        Construct a Point from a state list of integers.
        This is used by the neighbors method.

        ex: Point.from_state([0, 0, 0, 1, 2])
        This describes the start condition for the example puzzle.
        """
        elevator, *items = state
        pairs = len(items) // 2
        microchips, generators = tuple(items[:pairs]), tuple(items[pairs:])
        return cls(elevator=elevator,
                   microchips=microchips, generators=generators)

    def to_state(self):
        """
        Transform into an ordered list of floors for each component.
        """
        return [self.elevator, *self.microchips, *self.generators]

    def neighbors(self):
        """
        Find all the possible moves from a current position.
        Rules from the puzzle:
        -Use the elevator to move one or two pieces only,
        -The elevator moves one floor up or down at a time.

        Return a list of new valid points in descending order.
        """
        elevator, *items = self.to_state()
        states = []
        idxs = [i for i, x in enumerate(items) if x == elevator]
        combos = combinations(idxs, 2)
        for combo in combos:  # move two pieces up
            states.append([elevator + 1] + [x + 1 if i in combo else x
                                            for i, x in enumerate(items)])
        for idx, dir in product(idxs, (1, -1)):  # move one piece up or down
            states.append([elevator + dir] + [x + dir if i == idx else x
                                              for i, x in enumerate(items)])

        points = [Point.from_state(state) for state in states]
        return sorted((p for p in points if p.is_valid()), reverse=True)

    def is_valid(self):
        """
        Check that a point meets all puzzle criteria.
        """
        return (self.elevator_is_ok() and
                self.microchips_are_safe() and
                self.in_bounds())  # boundary is hardcoded :(

    def in_bounds(self, lower=0, upper=4):
        """
        All items in the point are on a floor in [lower, upper).
        """
        elevator, microchips, generators = self
        return (lower <= elevator < upper and
                all(lower <= m < upper for m in microchips) and
                all(lower <= g < upper for g in generators))

    def microchips_are_safe(self):
        """
        All microchips are safe if they are paired with their generator
        and/or not with any other generators.
        """
        elevator, microchips, generators = self
        for i, chip_floor in enumerate(microchips):
            if chip_floor == generators[i]:
                continue
            for generator_floor in generators:
                if chip_floor == generator_floor:
                    return False
        return True

    def elevator_is_ok(self):
        """
        The elevator can't be on a floor with nothing else.
        """
        elevator, microchips, generators = self
        return (elevator in microchips) or (elevator in generators)

    def cost(self, other):
        """
        The cost to move is always 1 in this puzzle.
        """
        return 1


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    def example():
        start = Point(elevator=0, microchips=(0, 0), generators=(1, 2))
        goal = Point(elevator=3, microchips=(3, 3), generators=(3, 3))
        return start, goal

    def part1():
        start = Point(elevator=0,
                      microchips=(0, 2, 2, 2, 2), generators=(0, 1, 1, 1, 1))
        goal = Point(elevator=3,
                     microchips=(3, 3, 3, 3, 3), generators=(3, 3, 3, 3, 3))
        return start, goal

    start, goal = part1()

    came_from, cost_so_far = Search.a_star(start, goal)
    path = Search.reconstruct_path(came_from, start, goal)

    for i, p in enumerate(path):
        print(p)

    print(len(path) - 1)

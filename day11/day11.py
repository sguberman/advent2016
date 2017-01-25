import heapq
from collections import namedtuple


#Point = namedtuple('Point', 'elevator microchips generators')
# ex: start = Point(elevator=0, microchips=(0, 0), generators=(1, 2))
# This is how a node in the graph is represented.
# Each integer denotes floors for each type of component.
# The microchips and generators are in the same order.


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]


def a_star_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {start: None}
    cost_so_far = {start: 0}

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for new in current.neighbors():
            new_cost = cost_so_far[current] + current.cost(new)
            if new not in cost_so_far or new_cost < cost_so_far[new]:
                cost_so_far[new] = new_cost
                priority = new_cost + heuristic(new, goal)
                frontier.put(new, priority)
                came_from[new] = current

    return came_from, cost_so_far


def reconstruct_path(came_from, start, goal):
    current = goal
    path = [current]
    while current != start:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path


class Point(namedtuple('Point', 'elevator microchips generators')):
    def neighbors(self):
        pass

    def in_bounds(self, lower, upper):
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
        return 1


def heuristic(point1, point2):
    return 1  # fix!

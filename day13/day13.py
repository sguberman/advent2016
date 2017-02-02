import heapq
import logging
from collections import namedtuple


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def __len__(self):
        return len(self.elements)

    def empty(self):
        return len(self) == 0

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
            logging.info('f: {} cf: {} '.format(len(frontier), len(came_from)))
            current = frontier.get()
            logging.debug('{}'.format(current))

            if current == goal:
                logging.debug('breaking for goal')
                break

            for new in current.neighbors():
                new_cost = cost_so_far[current] + current.cost(new)
                if new not in cost_so_far or new_cost < cost_so_far[new]:
                    cost_so_far[new] = new_cost
                    priority = new_cost + new.heuristic(goal)
                    frontier.put(new, priority)
                    came_from[new] = current

        logging.debug('frontier: {}'.format(frontier.elements))
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


class Point(namedtuple('Point', 'x y secret')):
    def is_wall(self):
        """
        Determine whether a given `x,y` coordinate will be a wall or an open space.
        """
        x, y, secret = self.x, self.y, self.secret
        num = x*x + 3*x + 2*x*y + y + y*y + secret
        return bool(sum(1 for x in bin(num)[2:] if x == '1') % 2)

    def in_bounds(self):
        """
        No negative points allowed.
        """
        return self.x >= 0 and self.y >= 0

    def heuristic(self, other):
        """
        Estimate the distance to the goal.
        """
        return abs(other.x - self.x) + abs(other.y - self.y)

    def cost(self, other):
        """
        All moves have a cost of 1 in this case.
        """
        return 1

    def neighbors(self):
        """
        Neighbors to the right, up, left, and down. No walls. No negative points.
        """
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        result = []
        for dir in dirs:
            neighbor = Point(self.x + dir[0], self.y + dir[1], self.secret)
            if neighbor.in_bounds() and not neighbor.is_wall():
                result.append(neighbor)
        return result


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    def example():
        start = Point(1, 1, 10)
        goal = Point(7, 4, 10)
        return start, goal

    def part1():
        start = Point(1, 1, 1364)
        goal = Point(31, 39, 1364)
        return start, goal

    start, goal = part1()

    came_from, cost_so_far = Search.a_star(start, goal)
    path = Search.reconstruct_path(came_from, start, goal)

    for point in path:
        print(point)

    print(len(path) - 1)

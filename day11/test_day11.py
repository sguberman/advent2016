from day11 import Point, a_star_search, reconstruct_path


class TestPoint:

    start = Point(elevator=0, microchips=(0, 0), generators=(1, 2))
    goal = Point(elevator=3, microchips=(3, 3), generators=(3, 3))
    danger = Point(elevator=0, microchips=(0, 0), generators=(0, 1))
    lonely = Point(elevator=2, microchips=(1, 1), generators=(3, 3))
    step1 = Point(elevator=1, microchips=(1, 0), generators=(1, 2))
    step2 = Point(elevator=2, microchips=(2, 0), generators=(2, 2))
    step3 = Point(elevator=1, microchips=(1, 0), generators=(2, 2))

    def test_in_bounds(self):
        assert self.start.in_bounds(0, 4)
        assert self.goal.in_bounds(0, 4)
        assert self.start.in_bounds(0, 3)
        assert not self.goal.in_bounds(0, 3)
        assert not self.start.in_bounds(0, 2)
        assert self.goal.in_bounds(3, 4)

    def test_microchips_are_safe(self):
        assert self.start.microchips_are_safe()
        assert self.goal.microchips_are_safe()
        assert not self.danger.microchips_are_safe()

    def test_elevator_is_ok(self):
        assert self.start.elevator_is_ok()
        assert self.goal.elevator_is_ok()
        assert not self.lonely.elevator_is_ok()

    def test_neighbors(self):
        start_neighbors = (
            self.step1,

        )
        assert self.start.neighbors() == sorted(start_neighbors, reverse=True)

        goal_neighbors = (
            Point(elevator=2, microchips=(2, 3), generators=(3, 3)),
            Point(elevator=2, microchips=(3, 2), generators=(3, 3)),
        )
        assert self.goal.neighbors() == sorted(goal_neighbors, reverse=True)

        step1_neighbors = (
            self.step2,
            self.start,
            Point(elevator=2, microchips=(1, 0), generators=(2, 2)),
        )
        assert self.step1.neighbors() == sorted(step1_neighbors, reverse=True)

        step2_neighbors = (
            self.step3,
            Point(elevator=3, microchips=(3, 0), generators=(2, 2)),
            Point(elevator=3, microchips=(3, 0), generators=(3, 2)),
            Point(elevator=3, microchips=(2, 0), generators=(3, 3)),
            Point(elevator=3, microchips=(2, 0), generators=(2, 3)),
            Point(elevator=1, microchips=(2, 0), generators=(2, 1)),
        )
        assert self.step2.neighbors() == sorted(step2_neighbors, reverse=True)

    def test_from_state(self):
        assert Point.from_state([0, 0, 0, 1, 2]) == self.start
        assert Point.from_state([3, 3, 3, 3, 3]) == self.goal

    def test_is_valid(self):
        assert self.start.is_valid()
        assert self.goal.is_valid()
        assert self.step1.is_valid()
        assert self.step2.is_valid()
        assert self.step3.is_valid()
        assert not self.danger.is_valid()
        assert not self.lonely.is_valid()


def test_example():
    start = Point(elevator=0, microchips=(0, 0), generators=(1, 2))
    goal = Point(elevator=3, microchips=(3, 3), generators=(3, 3))

    came_from, cost_so_far = a_star_search(start, goal)
    path = reconstruct_path(came_from, start, goal)

    for i, p in enumerate(path):
        print(p)
    assert len(path) - 1 == 11

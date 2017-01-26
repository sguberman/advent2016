from day11 import Point


class TestPoint:

    start = Point(elevator=0, microchips=(0, 0), generators=(1, 2))
    goal = Point(elevator=3, microchips=(3, 3), generators=(3, 3))
    danger = Point(elevator=0, microchips=(0, 0), generators=(0, 1))
    lonely = Point(elevator=2, microchips=(1, 1), generators=(3, 3))

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

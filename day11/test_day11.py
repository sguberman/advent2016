from day11 import Node, heuristic_cost_estimate, is_safe


class TestNode:
    start = Node.fromfloors('E mH mLi',
                            'gH',
                            'gLi',
                            '')

    goal = Node.fromfloors('',
                           '',
                           '',
                           'E gH mH gLi mLi')

    def test_node_fromfloors(self):
        assert len(self.start) == 4
        assert len(self.goal) == 4

    def test_heuristic_cost_estimate(self):
        assert heuristic_cost_estimate(self.start, self.goal) == 12

    def test_is_safe(self):
        for floor in self.start:
            assert is_safe(floor)

        for floor in self.goal:
            assert is_safe(floor)

        danger = Node.fromfloors('E mH gLi',
                                 'gH',
                                 'mLi',
                                 '')

        assert not is_safe(danger[0])
        for floor in danger[1:]:
            assert is_safe(floor)

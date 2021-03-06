from day11 import Node, heuristic_cost_estimate, is_safe, neighbors, a_star


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
        assert heuristic_cost_estimate(self.start, self.goal) == 6

    def test_is_safe(self):
        for floor in self.start:
            assert is_safe(floor)

        for floor in self.goal:
            assert is_safe(floor)

        danger = Node.fromfloors('E mH gLi',  # chip alone with other generator
                                 'gH',
                                 'mLi',
                                 '')

        assert not is_safe(danger[0])
        for floor in danger[1:]:
            assert is_safe(floor)

    def test_equivalence(self):
        assert self.start != self.goal
        s = set()
        s.add(self.start)
        assert self.goal not in s

        start2 = Node.fromfloors('E mLi mH',
                                 'gH',
                                 'gLi',
                                 '')  # same contents different order 1st floor
        assert start2 == self.start
        assert start2 in s

    def test_neighbors(self):
        n = list(neighbors(self.start, self.goal))
        assert len(n) == 1
        n1 = Node.fromfloors('mLi', 'E mH gH', 'gLi', '')
        assert n1 in n

        n = list(neighbors(n1, self.goal))
        assert len(n) == 3
        n2 = Node.fromfloors('mLi', '', 'E gH mH gLi', '')
        assert n2 in n

        n = list(neighbors(n2, self.goal))
        assert len(n) == 8
        n3 = Node.fromfloors('mLi', 'E mH', 'gH gLi', '')
        assert n3 in n

    def test_example(self):
        path = a_star(self.start, self.goal)
        for step in reversed(path):
            print('-------------')
            print(step)
        assert len(path) - 1 == 11

    def test_cost_compare(self):
        n1 = Node.fromfloors('mLi', 'E mH', 'gH gLi', '')
        n2 = Node.fromfloors('mLi', 'E gH gLi', 'mH', '')
        n1h = heuristic_cost_estimate(n1, self.goal)
        n2h = heuristic_cost_estimate(n2, self.goal)
        assert n1h < n2h

'''
class TestPart1:
    start = Node.fromfloors('E gPr mPr',
                            'gCo gCu gRu gPu',
                            'mCo mCu mRu mPu',
                            '')

    goal = Node.fromfloors('',
                           '',
                           '',
                           'E gPr mPr gCo mCo gCu mCu gRu mRu gPu mPu')

    def test_part1_path(self):
        path = a_star(self.start, self.goal)
        for step in reversed(path):
            print('##############')
            print(step)
        assert len(path) - 1 == 99999
'''

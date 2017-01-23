from .day11 import node


class TestRTGFacility:
    start = node('E mH mLi',
                 'gH',
                 'gLi',
                 '')

    goal = node('',
                '',
                '',
                'E gH mH gLi mLi')

    def test_node(self):
        assert len(self.start) == 4
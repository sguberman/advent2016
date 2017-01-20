from day10 import Swarm


class TestInputs:

    def test_example_input(self):
        botswarm = Swarm('test_input.txt')
        assert botswarm.who_compares(5, 2) == 2

    def test_part1_input(self):
        botswarm = Swarm('input.txt')
        assert botswarm.who_compares(61, 17) == 147

    def test_part2_input(self):
        botswarm = Swarm('input.txt')
        assert botswarm.multiply_bins(0, 1, 2) == 55637


class TestSwarm:

    swarm = Swarm('test_input.txt')

    def test_bot_chip_values(self):
        bot_chips = [(0, (5, 3)),
                     (1, (3, 2)),
                     (2, (2, 5))]
        for bot, chips in bot_chips:
            assert all(chip in self.swarm.bots[bot].chips for chip in chips)

    def test_bin_chip_values(self):
        bin_chips = [(0, (5,)),
                     (1, (2,)),
                     (2, (3,))]
        for bin, chips in bin_chips:
            assert all(chip in self.swarm.bins[bin].chips for chip in chips)

from collections import defaultdict


class Swarm:
    """
    A network of Bots and output Bins constructed from puzzle input.
    """
    def __init__(self, filename):
        self.bots = defaultdict(Bot)
        self.bins = defaultdict(Bin)

        with open(filename, 'r') as infile:
            for line in infile:
                self.parse(line)

    def parse(self, line):
        tokens = line.split()
        if line.startswith('value'):
            chipval = int(tokens[1])
            botnum = int(tokens[5])
            self.bots[botnum].getchip(chipval)
        else:
            botnum = int(tokens[1])
            lowtype = self.bots if tokens[5] == 'bot' else self.bins
            lownum = int(tokens[6])
            hightype = self.bots if tokens[10] == 'bot' else self.bins
            highnum = int(tokens[11])
            self.bots[botnum].low_to = lowtype[lownum]
            self.bots[botnum].high_to = hightype[highnum]
            self.bots[botnum].givechips()

    def who_compares(self, *chips):  # part 1
        for botnum, bot in self.bots.items():
            if sorted(bot.chips) == sorted(chips):
                return botnum

    def multiply_bins(self, *binnums):  # part 2
        product = 1
        for binnum in binnums:
            if len(self.bins[binnum].chips) == 1:
                product *= self.bins[binnum].chips[0]
        return product


class Bin:
    """
    A Bin can only receive chips.
    """
    def __init__(self):
        self.chips = []

    def getchip(self, chipnum):
        self.chips.append(chipnum)


class Bot(Bin):
    """
    A Bot compares two chip numbers and delivers the chips to another Bot
    or an output Bin.
    """
    def __init__(self):
        super().__init__()
        self.low_to = None
        self.high_to = None

    def getchip(self, chipnum):
        super().getchip(chipnum)
        self.givechips()

    def givechips(self):
        if len(self.chips) > 1 and self.low_to and self.high_to:
            self.low_to.getchip(min(self.chips))
            self.high_to.getchip(max(self.chips))


if __name__ == '__main__':
    botswarm = Swarm('input.txt')
    print(botswarm.who_compares(61, 17))  # part 1
    print(botswarm.multiply_bins(0, 1, 2))  # part 2

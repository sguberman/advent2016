class Disc:
    def __init__(self, positions, start):
        self.positions = positions
        self.start = start

    def at_time(self, time):
        return (self.start + time) % self.positions

    @classmethod
    def from_input(cls, line):
        tokens = line.split()
        positions, start = map(int, (tokens[3], tokens[-1][:-1]))
        return cls(positions, start)

    def __eq__(self, other):
        return self.positions, self.start == other.positions, other.start


class Maze:
    def __init__(self, filename):
        self.discs = []
        with open(filename, 'r') as input:
            for line in input:
                self.discs.append(Disc.from_input(line))

    def solve(self):
        time = 0
        while any(d.at_time(time + i + 1) for i, d in enumerate(self.discs)):
            time += 1
        return time

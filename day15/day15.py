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

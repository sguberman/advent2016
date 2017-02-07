class Disc:
    def __init__(self, positions, start):
        self.positions = positions
        self.start = start

    def at_time(self, time):
        return (self.start + time) % self.positions

class Facility:
    def __init__(self, *floors):
        contents = []
        self.elevator_on = 0
        for i, floor in enumerate(floors):
            items = floor.split()
            if 'E' in items:
                self.elevator_on = i
                items.remove('E')
            contents.append(tuple(sorted(items)))
        self.contents = tuple(contents)

    def display(self):
        floorstrings = []
        for i, items in enumerate(self.contents):
            floornum = i + 1
            marker = '[E]' if i == self.elevator_on else '[:]'
            itemstr = ' '.join(items)
            floorstrings.append(f'{floornum} {marker} {itemstr}')
        print('\n'.join(reversed(floorstrings)))

    def __hash__(self):
        return hash((self.elevator_on,) + self.contents)
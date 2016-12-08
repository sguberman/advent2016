def move(x, y, facing, instruction):
    direction, steps = instruction[0], instruction[1:]
    steps = int(steps)
    if facing == 'north':
        if direction == 'R':
            x += steps
            facing = 'east'
        elif direction == 'L':
            x -= steps
            facing = 'west'
    elif facing == 'south':
        if direction == 'R':
            x -= steps
            facing = 'west'
        elif direction == 'L':
            x += steps
            facing = 'east'
    elif facing == 'west':
        if direction == 'R':
            y += steps
            facing = 'north'
        elif direction == 'L':
            y -= steps
            facing = 'south'
    elif facing == 'east':
        if direction == 'R':
            y -= steps
            facing = 'south'
        elif direction == 'L':
            y += steps
            facing = 'north'
    return x, y, facing


def walk(instructions, facing='north'):
    x, y = (0, 0)
    for instr in instructions:
        x, y, facing = move(x, y, facing, instr)
    return x, y, facing


def distance(x, y):
    return abs(x) + abs(y)


def part1(instructions):
    x, y, facing = walk(instructions)
    dist = distance(x, y)
    return dist


if __name__ == '__main__':
    with open('day1.txt', 'r') as f:
        instructions = f.read().split(', ')
    dist = part1(instructions)
    print(dist)


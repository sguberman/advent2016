def move(on, instruction, keypad):
    for i, row in enumerate(keypad):
        try:
            j = row.index(on)
            break
        except ValueError:
            continue
    if instruction == 'U':
        i -= 1
        if i < 0:
            i = 0
    elif instruction == 'D':
        i += 1
    elif instruction == 'L':
        j -= 1
        if j < 0:
            j = 0
    elif instruction == 'R':
        j += 1
    try:
        if keypad[i][j] != -1:
            return keypad[i][j]
        else:
            return on
    except IndexError:
        return on


def digit(on, instructions, keypad):
    for instruction in instructions:
        on = move(on, instruction, keypad)
    return on


def keycode(filename, keypad=None, start=5):
    if keypad is None:
        keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    with open(filename, 'r') as instructions:
        on = start
        code = ''
        for line in instructions:
            on = digit(on, line, keypad)
            code += str(on)
    return code


if __name__ == '__main__':
    print(keycode('input.txt'))
    keypad = [[-1, -1, 1, -1, -1],
              [-1, 2, 3, 4, -1],
              [5, 6, 7, 8, 9],
              [-1, 'A', 'B', 'C', -1],
              [-1, -1, 'D', -1, -1]]
    print(keycode('input.txt', keypad))

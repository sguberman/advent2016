def dragon(a):
    b = ''.join('1' if x == '0' else '0' for x in reversed(a))
    return a + '0' + b


def checksum(data):
    return ''.join('1' if a == b else '0' for a, b in zip(data[::2], data[1::2]))


def solve(length, initial_state):
    raise NotImplementedError


if __name__ == '__main__':
    print(solve(272, '01111010110010011'))


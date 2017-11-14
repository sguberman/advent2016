def dragon(a):
    b = ''.join('1' if x == '0' else '0' for x in reversed(a))
    return a + '0' + b


def checksum(data):
    raise NotImplementedError


def solve(length, initial_state):
    raise NotImplementedError


if __name__ == '__main__':
    print(solve(272, '01111010110010011'))


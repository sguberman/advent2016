def dragon(a):
    b = ''.join('1' if x == '0' else '0' for x in reversed(a))
    return a + '0' + b


def checksum(data):
    return ''.join('1' if a == b else '0' for a, b in zip(data[::2], data[1::2]))


def solve(length, data):
    while len(data) < length:
        data = dragon(data)
    data = data[:length]
    check = checksum(data)
    while len(check) % 2 == 0:
        check = checksum(check)
    return check


if __name__ == '__main__':
    print(solve(272, '01111010110010011'))
    print(solve(35651584, '01111010110010011'))


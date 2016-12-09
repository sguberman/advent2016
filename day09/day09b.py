from itertools import islice, takewhile


def decompression_size(text, recursively=False):
    result = 0
    chars = iter(text)
    for c in chars:
        if c == '(':
            num = int(''.join(takewhile(lambda _: _ != 'x', chars)))
            times = int(''.join(takewhile(lambda _: _ != ')', chars)))
            s = ''.join(islice(chars, num))
            result += (decompression_size(s, recursively) if recursively else len(s)) * times
        else:
            result += 1
    return result


if __name__ == '__main__':
    with open('input.txt', 'r') as input_file:
        text = input_file.read().strip()
    print(decompression_size(text))
    print(decompression_size(text, recursively=True))

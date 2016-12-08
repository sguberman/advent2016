from collections import Counter, defaultdict


def main(filename):
    with open(filename, 'r') as noise:
        columns = defaultdict(Counter)
        for line in noise:
            for i, letter in enumerate(line.strip()):
                columns[i].update(letter)
    message = ''
    for col in sorted(columns.keys()):
        message += columns[col].most_common()[0][0]
    return message


def main2(filename):
    with open(filename, 'r') as noise:
        columns = defaultdict(Counter)
        for line in noise:
            for i, letter in enumerate(line.strip()):
                columns[i].update(letter)
    message = ''
    for col in sorted(columns.keys()):
        message += columns[col].most_common()[-1][0]
    return message

if __name__ == '__main__':
    print(main('input.txt'))
    print(main2('input.txt'))


def decompress(text):
    text = list(text)
    decompressed = []
    mode = 'normal'
    marker = []
    while text:
        if mode == 'normal':
            w = text.pop(0)
            if w != '(':
                decompressed.append(w)
            else:
                mode = 'marker'
        elif mode == 'marker':
            w = text.pop(0)
            if w != ')':
                marker.append(w)
            else:
                num, times = parse_marker(marker)
                marker = []
                mode = 'decompress'
        elif mode == 'decompress':
            stack = [text.pop(0) for _ in range(num)] * times
            decompressed.extend(stack)
            mode = 'normal'
    return ''.join(decompressed)


def parse_marker(marker):
    marker = ''.join(marker)
    num, times = marker.split('x')
    num, times = int(num), int(times)
    return num, times


def decompressed_file_len(filename):
    with open(filename, 'r') as f:
        decompressed = decompress(f.read().strip())
    return len(decompressed)


def decompressed_file_len2(filename, save_final=False, save_tmp=False):
    with open(filename, 'r') as f:
        text = f.read().strip()
    while '(' in text:
        text = decompress(text)
        if save_tmp:
            with open('temp.txt', 'w') as temp:
                temp.write(text)
    if save_final:
        with open('decompressed_'+filename, 'w') as dec:
            dec.write(text)
    return len(text)


if __name__ == '__main__':
    print(decompressed_file_len('input.txt'))
    print(decompressed_file_len2('input.txt'))

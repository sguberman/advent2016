from hashlib import md5


def hash_hex(salt, idx, stretch=0):
    h = md5(bytes(salt + str(idx), encoding='utf-8')).hexdigest()
    for _ in range(stretch):
        h = md5(bytes(h, encoding='utf-8')).hexdigest()
    return h


def first_triple(hexdigest):
    for (a, b, c) in zip(hexdigest, hexdigest[1:], hexdigest[2:]):
        if a == b == c:
            return a
    return False


def has_consecutive_digit(hexdigest, digit, times=5):
    return times * digit in hexdigest


def is_key(salt, idx, hashes=None, window=1000, stretching=0):
    if hashes is None:
        hashes = []
    try:
        key = hashes[idx]
    except IndexError:
        key = hash_hex(salt, idx, stretching)
        hashes.append(key)
    digit = first_triple(key)
    if not digit:
        return False, hashes
    for i in range(idx + 1, idx + window + 1):
        try:
            hexdigest = hashes[i]
        except IndexError:
            hexdigest = hash_hex(salt, i, stretching)
            hashes.append(hexdigest)
        if has_consecutive_digit(hexdigest, digit):
            return key, hashes
    return False, hashes


def generate_n_keys(salt, n=64, start_idx=0, window=1000, stretching=0):
    up_to = n
    n = 0
    idx = start_idx
    known_hashes = None
    while n < up_to:
        key, known_hashes = is_key(salt, idx, known_hashes, window, stretching)
        if key:
            n += 1
            yield key, idx
        idx += 1


if __name__ == '__main__':
    #keys = list(generate_n_keys('ahsbgdzn', n=64))
    keys = list(generate_n_keys('ahsbgdzn', n=64, stretching=2016))
    key, idx = keys[-1]
    print(idx, key)

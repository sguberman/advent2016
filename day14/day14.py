from hashlib import md5


def hash_hex(salt, idx):
    return md5(bytes(salt + str(idx), encoding='utf-8')).hexdigest()


def first_triple(hexdigest):
    for (a, b, c) in zip(hexdigest, hexdigest[1:], hexdigest[2:]):
        if a == b == c:
            return a
    return False


def has_consecutive_digit(hexdigest, digit, times=5):
    return times * digit in hexdigest


def is_key(salt, idx, hashes=None, window=1000):
    if hashes is None:
        hashes = []
    return False, hashes

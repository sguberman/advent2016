import pytest
from day14 import (hash_hex, first_triple, has_consecutive_digit, is_key,
                   generate_n_keys)


@pytest.mark.parametrize('salt,idx,expected', [
    ('abc', 18, '8'),
    ('abc', 39, 'e'),
    ('abc', 816, 'e'),
    ('abc', 92, '9'),
    ('abc', 200, '9'),
    ('abc', 22728, 'c'),
])
def test_hash_and_first_triple(salt, idx, expected):
    assert first_triple(hash_hex(salt, idx)) == expected


@pytest.mark.parametrize('salt,idx,digit', [
    ('abc', 816, 'e'),
    ('abc', 200, '9'),
    pytest.mark.xfail(('abc', 18, '8')),
    pytest.mark.xfail(('abc', 39, 'e')),
    pytest.mark.xfail(('abc', 92, '9')),
    pytest.mark.xfail(('abc', 22728, 'c')),
])
def test_has_consectutive_digit(salt, idx, digit):
    assert has_consecutive_digit(hash_hex(salt, idx), digit)


@pytest.mark.parametrize('salt,idx', [
    pytest.mark.xfail(('abc', 18)),
    ('abc', 39),
    ('abc', 92),
    ('abc', 22728),
])
def test_is_key(salt, idx):
    result, hashes = is_key(salt, idx, hashes=[])
    assert result


def test_generate_n_keys():
    keys = [key for key in generate_n_keys('abc', n=64)]
    assert len(keys) == 64
    key, idx = keys[-1]
    print(idx, key)
    assert idx == 22728


@pytest.mark.parametrize('salt,idx,stretch,expected', [
    ('abc', 0, 0, '577571be4de9dcce85a041ba0410f29f'),
    ('abc', 0, 1, 'eec80a0c92dc8a0777c619d9bb51e910'),
    ('abc', 0, 2, '16062ce768787384c81fe17a7a60c7e3'),
    ('abc', 0, 2016, 'a107ff634856bb300138cac6568c0f24'),
])
def test_hash_hex_stretching(salt, idx, stretch, expected):
    assert hash_hex(salt, idx, stretch) == expected


def test_generate_n_keys_with_stretching():
    keys = [key for key in generate_n_keys('abc', n=64, stretching=2016)]
    assert len(keys) == 64
    key, idx = keys[-1]
    print(idx, key)
    assert idx == 22551

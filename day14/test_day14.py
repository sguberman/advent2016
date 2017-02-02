import pytest
from day14 import hash_hex, first_triple, has_consecutive_digit, is_key


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

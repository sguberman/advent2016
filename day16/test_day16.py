import pytest

from day16 import dragon, checksum, solve


def test_dragon():
    assert dragon('1') == '100'
    assert dragon('0') == '001'
    assert dragon('11111') == '11111000000'
    assert dragon('111100001010') == '1111000010100101011110000'


def test_checksum():
    assert checksum('110010110100') == '110101'
    assert checksum('110101') == '100'


def test_solve():
    assert solve(20, '10000') == '01100'


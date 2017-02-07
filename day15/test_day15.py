import pytest
from day15 import Disc


@pytest.mark.parametrize('t,expected', [
    (0, 11),
    (1, 12),
    (2, 0),
    (3, 1),
    (4, 2),
    (5, 3),
    (6, 4),
    (7, 5),
    (8, 6),
    (9, 7),
    (10, 8),
    (11, 9),
    (12, 10),
    (13, 11),
    (14, 12),
    (15, 0),
])
def test_Disc_at_time(t, expected):
    d = Disc(positions=13, start=11)
    assert d.at_time(t) == expected

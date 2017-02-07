import pytest
from day15 import Disc, Maze


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


@pytest.mark.parametrize('line,expected', [
    ('Disc #1 has 13 positions; at time=0, it is at position 11.', Disc(13, 11)),
    ('Disc #2 has 5 positions; at time=0, it is at position 0.', Disc(5, 0)),
    ('Disc #3 has 17 positions; at time=0, it is at position 11.', Disc(17, 11)),
    ('Disc #4 has 3 positions; at time=0, it is at position 0.', Disc(3, 0)),
    ('Disc #5 has 7 positions; at time=0, it is at position 2.', Disc(7, 2)),
    ('Disc #6 has 19 positions; at time=0, it is at position 17.', Disc(19, 17)),
])
def test_Disc_from_input(line, expected):
    assert Disc.from_input(line) == expected


def test_Maze():
    assert Maze('test_input.txt').discs == [Disc(5, 4), Disc(2, 1)]


def test_Maze_solve():
    assert Maze('test_input.txt').solve() == 5
    assert Maze('input.txt').solve() == 122318

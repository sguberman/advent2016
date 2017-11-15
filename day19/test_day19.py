from day19 import white_elephant, steal_from_neighbor


def test_white_elephant():
    assert white_elephant(5) == 3
    assert white_elephant(3005290) == 0  # TODO


def test_steal_from_neighbor():
    start = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1}
    a = {1: 2, 2: 0, 3: 1, 4: 1, 5: 1}
    b = {1: 2, 2: 0, 3: 1, 4: 1, 5: 1}
    c = {1: 2, 2: 0, 3: 2, 4: 0, 5: 1}
    d = {1: 2, 2: 0, 3: 2, 4: 0, 5: 1}
    e = {1: 0, 2: 0, 3: 2, 4: 0, 5: 3}
    final = {1: 0, 2: 0, 3: 5, 4: 0, 5: 0}
    assert steal_from_neighbor(start, 1) == a
    assert steal_from_neighbor(a, 2) == b
    assert steal_from_neighbor(b, 3) == c
    assert steal_from_neighbor(c, 4) == d
    assert steal_from_neighbor(d, 5) == e
    assert steal_from_neighbor(e, 3) == final


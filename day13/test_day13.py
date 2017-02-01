from day13 import is_wall


def test_is_wall():
    assert not is_wall(0, 0)
    assert is_wall(1, 0)
    assert not is_wall(2, 0)

from day02 import move, digit, keycode


keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def test_move():
    assert move(5, 'U', keypad) == 2
    assert move(5, 'D', keypad) == 8
    assert move(5, 'L', keypad) == 4
    assert move(5, 'R', keypad) == 6


def test_move_on_edges():
    assert move(2, 'U', keypad) == 2
    assert move(8, 'D', keypad) == 8
    assert move(4, 'L', keypad) == 4
    assert move(6, 'R', keypad) == 6


def test_one_line():
    assert digit(5, 'ULL', keypad) == 1
    assert digit(1, 'RRDDD', keypad) == 9
    assert digit(9, 'LURDL', keypad) == 8
    assert digit(8, 'UUUUD', keypad) == 5


def test_full_entry():
    assert keycode('test_input.txt') == '1985'
    assert keycode('input.txt') == '92435'


def test_weird_keypad():
    keypad = [[-1, -1, 1, -1, -1],
              [-1, 2, 3, 4, -1],
              [5, 6, 7, 8, 9],
              [-1, 'A', 'B', 'C', -1],
              [-1, -1, 'D', -1, -1]]
    assert keycode('test_input.txt', keypad) == '5DB3'
    assert keycode('input.txt', keypad) == 'C1A88'

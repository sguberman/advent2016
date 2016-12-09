from day08 import Screen
import numpy as np


class TestScreenMethods:
    scr = Screen(7, 3)

    def test_init(self):
        iscr = Screen(7, 3)
        result = np.zeros((3, 7))
        assert (iscr.pixels == result).all()

    def test_rect(self):
        self.scr.rect(3, 2)
        result = np.array([[1, 1, 1, 0, 0, 0, 0],
                           [1, 1, 1, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0]])
        assert (self.scr.pixels == result).all()

    def test_rotate_column(self):
        self.scr.rotate_column(1, 1)
        result = np.array([[1, 0, 1, 0, 0, 0, 0],
                           [1, 1, 1, 0, 0, 0, 0],
                           [0, 1, 0, 0, 0, 0, 0]])
        assert (self.scr.pixels == result).all()

    def test_rotate_row(self):
        self.scr.rotate_row(0, 4)
        result = np.array([[0, 0, 0, 0, 1, 0, 1],
                           [1, 1, 1, 0, 0, 0, 0],
                           [0, 1, 0, 0, 0, 0, 0]])
        assert (self.scr.pixels == result).all()

    def test_rotate_column_again(self):
        self.scr.rotate_column(1, 1)
        result = np.array([[0, 1, 0, 0, 1, 0, 1],
                           [1, 0, 1, 0, 0, 0, 0],
                           [0, 1, 0, 0, 0, 0, 0]])
        assert (self.scr.pixels == result).all()

    def test_count_pixels(self):
        assert self.scr.count_pixels() == 6


class TestScreenInterpreter:
    scr = Screen(7, 3)

    def test_interpret_rect(self):
        self.scr.interpret('rect 3x2')
        result = np.array([[1, 1, 1, 0, 0, 0, 0],
                           [1, 1, 1, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0]])
        assert (self.scr.pixels == result).all()

    def test_interpret_rotate_column(self):
        self.scr.interpret('rotate column x=1 by 1')
        result = np.array([[1, 0, 1, 0, 0, 0, 0],
                           [1, 1, 1, 0, 0, 0, 0],
                           [0, 1, 0, 0, 0, 0, 0]])
        assert (self.scr.pixels == result).all()

    def test_interpret_rotate_row(self):
        self.scr.interpret('rotate row y=0 by 4')
        result = np.array([[0, 0, 0, 0, 1, 0, 1],
                           [1, 1, 1, 0, 0, 0, 0],
                           [0, 1, 0, 0, 0, 0, 0]])
        assert (self.scr.pixels == result).all()


class TestScreenDecodeInput:
    def test_example_input(self):
        scr = Screen(7, 3)
        scr.decode('test_input.txt')
        pixels = np.array([[0, 1, 0, 0, 1, 0, 1],
                           [1, 0, 1, 0, 0, 0, 0],
                           [0, 1, 0, 0, 0, 0, 0]])
        assert (scr.pixels == pixels).all()
        assert scr.count_pixels() == 6

    def test_actual_input(self):
        scr = Screen(50, 6)
        scr.decode('input.txt')
        assert scr.count_pixels() == 123

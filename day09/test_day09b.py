from day09b import decompression_size

import pytest


CASES = [('ADVENT', False, 6),
         ('A(1x5)BC', False, 7),
         ('(3x3)XYZ', False, 9),
         ('A(2x2)BCD(2x2)EFG', False, 11),
         ('(6x1)(1x3)A', False, 6),
         ('X(8x2)(3x3)ABCY', False, 18),
         ('(3x3)XYZ', True, 9),
         ('X(8x2)(3x3)ABCY', True, 20),
         ('(27x12)(20x12)(13x14)(7x10)(1x12)A', True, 241920),
         ('(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN', True, 445)
         ]


@pytest.mark.parametrize('text, recursively, size', CASES)
def test_decompression_size_examples(text, recursively, size):
    assert decompression_size(text, recursively) == size


def test_part1_input():
    text = open('input.txt').read().strip()
    assert decompression_size(text) == 70186


def test_part2_input():
    text = open('input.txt').read().strip()
    assert decompression_size(text, recursively=True) == 10915059201

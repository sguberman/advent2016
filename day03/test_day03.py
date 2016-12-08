from day03 import is_triangle, count_triangles, count_triangles_vertically


def test_is_triangle():
    assert is_triangle(3, 4, 5) == True
    assert is_triangle(5, 10, 25) == False


def test_count_triangles():
    assert count_triangles('test_input.txt') == 0
    assert count_triangles('input.txt') == 1050


def test_count_triangles_vertically():
    assert count_triangles_vertically('test_input2.txt') == 6
    assert count_triangles_vertically('input.txt') == 1921

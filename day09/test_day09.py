from day09 import decompress, parse_marker, decompressed_file_len


def test_decompress():
    with open('test_input.txt', 'r') as test_cases:
        for test in test_cases:
            compressed, decompressed, length = test.strip().split()
            #print(compressed, decompressed, length)
            length = int(length)
            assert decompress(compressed) == decompressed
            assert len(decompressed) == length


def test_parse_marker():
    assert parse_marker(list('1x5')) == (1, 5)
    assert parse_marker(list('3x3')) == (3, 3)
    assert parse_marker(list('2x2')) == (2, 2)
    assert parse_marker(list('4275x11')) == (4275, 11)


def test_decompressed_file_len():
    assert decompressed_file_len('test_input2.txt') == 57
    assert decompressed_file_len('input.txt') == 70186

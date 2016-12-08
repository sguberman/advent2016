from day04 import is_real, parse_room, sector_id_sum, decrypt, sector_id_from_keywords


def test_is_real():
    assert is_real('aaaaa-bbb-z-y-x', 'abxyz') == True
    assert is_real('a-b-c-d-e-f-g-h', 'abcde') == True
    assert is_real('not-a-real-room', 'oarel') == True
    assert is_real('totally-real-room', 'decoy') == False


def test_parse_room():
    assert parse_room('aaaaa-bbb-z-y-x-123[abxyz]') == ('aaaaa-bbb-z-y-x', 123, 'abxyz')
    assert parse_room('a-b-c-d-e-f-g-h-987[abcde]') == ('a-b-c-d-e-f-g-h', 987, 'abcde')
    assert parse_room('not-a-real-room-404[oarel]') == ('not-a-real-room', 404, 'oarel')
    assert parse_room('totally-real-room-200[decoy]') == ('totally-real-room', 200, 'decoy')


def test_sector_id_sum():
    assert sector_id_sum('test_input.txt') == (123 + 987 + 404)
    assert sector_id_sum('input.txt') == 173787


def test_decrypt():
    assert decrypt('qzmt-zixmtkozy-ivhz', 343) == 'very encrypted name'


def test_sector_id_from_keywords():
    assert sector_id_from_keywords('input.txt', 'north pole object') == 548

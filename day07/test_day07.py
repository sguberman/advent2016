from day07 import count_tls, supports_tls, find_hypernets, has_abba


def test_count_tls():
    assert count_tls('test_input.txt') == 3
    assert count_tls('input.txt') == 118


def test_supports_tls():
    assert supports_tls('abba[mnop]qrst')
    assert not supports_tls('abcd[bddb]xyyx')
    assert not supports_tls('aaaa[qwer]tyui')
    assert supports_tls('ioxxoj[asdfgh]zxcvbn')
    assert supports_tls('ioxxoj[asdfgh]zxcvbnaaaa[qwer]tyui')


def test_find_hypernets():
    assert find_hypernets('abba[mnop]qrst') == ['mnop']
    assert find_hypernets('abcd[bddb]xyyx') == ['bddb']
    assert find_hypernets('aaaa[qwer]tyui') == ['qwer']
    assert find_hypernets('ioxxoj[asdfgh]zxcvbn') == ['asdfgh']
    assert find_hypernets('abba[mnop]qrstabcd[bddb]xyyx') == ['mnop', 'bddb']


def test_has_abba():
    assert has_abba('abba[mnop]qrst')
    assert has_abba('abcd[bddb]xyyx')
    assert not has_abba('aaaa[qwer]tyui')
    assert has_abba('ioxxoj[asdfgh]zxcvbn')
    assert has_abba('ioxxoj[asdfgh]zxcvbnaaaa[qwer]tyui')

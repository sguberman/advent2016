from day07 import count_tls, supports_tls, find_hypernets, has_abba
from day07 import find_supernets, find_abas, supports_ssl, count_ssl


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


def test_find_supernets():
    assert find_supernets('abba[mnop]qrst') == {'abba', 'qrst'}
    assert find_supernets('abcd[bddb]xyyx') == {'abcd', 'xyyx'}
    assert find_supernets('aaaa[qwer]tyui') == {'aaaa', 'tyui'}
    assert find_supernets('abba[mnop]qrstabcd[bddb]xyyx') == {'abba', 'qrstabcd', 'xyyx'}


def test_find_abas():
    assert find_abas(['aba', 'bab', 'xyz']) == {'aba', 'bab'}
    assert find_abas(['zzz']) == set()
    assert find_abas(['zazbz', 'abc', 'brb']) == {'zaz', 'zbz', 'brb'}


def test_supports_ssl():
    assert supports_ssl('aba[bab]xyz')
    assert not supports_ssl('xyx[xyx]xyx')
    assert supports_ssl('aaa[kek]eke')
    assert supports_ssl('zazbz[bzb]cdb')


def test_count_ssl():
    assert count_ssl('test_input2.txt') == 3
    assert count_ssl('input.txt') == 260

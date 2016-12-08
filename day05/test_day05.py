from day05 import crack_password, crack_password2


def test_crack_password():
    assert crack_password('abc') == '18f47a30'
    assert crack_password('uqwqemis') == '1a3099aa'


def test_crack_password2():
    assert crack_password2('abc') == '05ace8e3'

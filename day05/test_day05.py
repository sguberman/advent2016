from day05 import crack_password, crack_password2
import unittest


class TestCrackPassword(unittest.TestCase):
    def test_crack_password(self):
        self.assertEqual(crack_password('abc'), '18f47a30')
        self.assertEqual(crack_password('uqwqemis'), '1a3099aa')

    def test_crack_password2(self):
        self.assertEqual(crack_password2('abc'), '05ace8e3')
        self.assertEqual(crack_password2('uqwqemis'), '694190cd')


if __name__ == '__main__':
    unittest.main()


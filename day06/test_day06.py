import unittest
from day06 import main, main2


class TestMain(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main('test_input.txt'), 'easter')
    
    
    def test_main2(self):
        self.assertEqual(main2('test_input.txt'), 'advent')

if __name__ == '__main__':
    unittest.main()


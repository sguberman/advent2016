import unittest
from day01 import walk, distance, part1


class TestDay1(unittest.TestCase):
    
    def test_walk(self):
        instructions = ['R2', 'L3']
        self.assertEqual(walk(instructions), (2, 3, 'north'))
        instructions = ['R2', 'R2', 'R2']
        self.assertEqual(walk(instructions), (0, -2, 'west'))
        instructions = ['R5', 'L5', 'R5', 'R3']
        self.assertEqual(walk(instructions), (10, 2, 'south'))
     
    def test_distance(self):
        self.assertEqual(distance(2, 3), 5)
        self.assertEqual(distance(0, -2), 2)
        self.assertEqual(distance(10, 2), 12)
    
    def test_part1(self):
        instructions = ['R2', 'L3']
        self.assertEqual(part1(instructions), 5)
        instructions = ['R2', 'R2', 'R2']
        self.assertEqual(part1(instructions), 2)
        instructions = ['R5', 'L5', 'R5', 'R3']
        self.assertEqual(part1(instructions), 12)


if __name__ == '__main__':
    unittest.main()


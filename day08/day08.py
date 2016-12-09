import re
import numpy as np
from collections import deque


class Screen:
    def __init__(self, width, height):
        self.pixels = np.zeros((height, width))

    def rect(self, width, height):
        self.pixels[:height, :width] = 1

    def rotate_column(self, column, by):
        pt = self.pixels.transpose()
        ptr = deque(pt[column])
        ptr.rotate(by)
        pt[column] = ptr
        self.pixels = pt.transpose()

    def rotate_row(self, row, by):
        pr = deque(self.pixels[row])
        pr.rotate(by)
        self.pixels[row] = pr

    def count_pixels(self):
        return np.sum(self.pixels)

    def interpret(self, command):
        if command.startswith('rect'):
            first, second = command.split()
            width, height = map(int, second.split('x'))
            self.rect(width, height)
        elif command.startswith('rotate column'):
            column = int(re.findall(r'=(\d+)', command)[0])
            by = int(re.findall(r'by (\d+)', command)[0])
            self.rotate_column(column, by)
        elif command.startswith('rotate row'):
            row = int(re.findall(r'=(\d+)', command)[0])
            by = int(re.findall(r'by (\d+)', command)[0])
            self.rotate_row(row, by)

    def decode(self, filename):
        with open(filename, 'r') as commands:
            for command in commands:
                self.interpret(command)

    def display(self):
        for row in self.pixels:
            print(''.join(['X' if val == 1 else '.' for val in row]))

if __name__ == '__main__':
    scr = Screen(50, 6)
    scr.decode('input.txt')
    print(scr.count_pixels())
    scr.display()

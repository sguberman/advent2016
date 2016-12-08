def is_triangle(a, b, c):
    return (a < b + c) and (b < a + c) and (c < a + b)


def count_triangles(filename):
    with open(filename, 'r') as triangles:
        count = 0
        for triangle in triangles:
            a, b, c = [int(x) for x in triangle.split()]
            if is_triangle(a, b, c):
                count += 1
    return count


def count_triangles_vertically(filename):
    with open(filename, 'r') as triangles:
        count = 0
        three_lines = [triangles.readline(), triangles.readline(), triangles.readline()]
        while three_lines[0]:
            #print(three_lines)
            three_triangles = [[], [], []]
            for line in three_lines:
                a1, a2, a3 = [int(x) for x in line.split()]
                three_triangles[0].append(a1)
                three_triangles[1].append(a2)
                three_triangles[2].append(a3)
            count += sum(is_triangle(*tri) for tri in three_triangles)
            three_lines = [triangles.readline(), triangles.readline(), triangles.readline()]
    return count


if __name__ == '__main__':
    print(count_triangles('input.txt'))
    print(count_triangles_vertically('input.txt'))

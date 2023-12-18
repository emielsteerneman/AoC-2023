# A combination of the Shoelace formula and Pick's theorem 
#
# Shoe-lace formula: Calculates the area of a polygon given the coordinates of its vertices
#   Area = 1/2 * (x1y2 + x2y3 + ... + xn-1yn + xny1 - x2y1 - x3y2 - ... - xnyn-1 - x1yn)
# 
# Pick's theorem: Calculates the area of a polygon given the number of points inside the 
# polygon (I) and the number of points on the boundary of the polygon (B)
#   Area = I + B/2 - 1
#
# What we need to know is I + B. B can simply be calculated by counting the number of
# points on the boundary of the polygon. I can be calculated by using Pick's theorem
#
# Calculating I:
#   A = Shoelace(coordinates)
#   B = boundary_length(coordinates)
# Then  
#   A = I + B/2 - 1 (Pick's theorem)
#   I = A + 1 - B/2
#   I = Shoelace(coordinates) + 1 - boundary_length(coordinates)/2
#
# Finally, the answer is I + B

import numpy as np
import matplotlib.pyplot as plt

def shoelace(c):
    sum_1, sum_2 = 0, 0
    for i in range(0, len(c)-1):
        sum_1 += c[i][0] * c[i+1][1]
        sum_2 += c[i][1] * c[i+1][0]
    return abs(sum_1 - sum_2) // 2

instructions = [ _.split(' ') for _ in open("input.txt").read().splitlines() ]

direction_map = { 'U' : (-1, 0), 'D' : (1, 0), 'L' : (0, -1), 'R' : (0, 1), '0' : (0, 1), '1' : (1, 0), '2' : (0, -1), '3' : (-1, 0) }

""" Part 1"""

coordinates = []
x, y, B = 0, 0, 0
for d, n, _ in instructions:
    n = int(n)
    dx, dy = direction_map[d]
    x, y, B = x + dx * n, y + dy * n, B + n
    coordinates.append((x, y))

A = shoelace(coordinates)
I = A + 1 - B // 2
print("Part 1:", I + B)

""" Part 2 """
coordinates = []
x, y, B = 0, 0, 0
for _, _, color in instructions:
    n, d = int(color[2:7], 16), color[7]
    dx, dy = direction_map[d]
    x, y, B = x + dx * n, y + dy * n, B + n
    coordinates.append((x, y))

A = shoelace(coordinates)
I = A + 1 - B // 2
print("Part 2:", I + B)
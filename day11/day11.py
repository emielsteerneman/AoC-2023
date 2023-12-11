import numpy as np
from itertools import combinations 

file = open("input.txt").read()

# Convert file to matrix with 0's and 1's
matrix = np.array([ list(map(".#".index, _)) for _ in file.splitlines() ])

# List of all empty rows and columns
R = np.where( ~matrix.any(axis=1)	)[0]
C = np.where( ~matrix.any(axis=0)	)[0]

# Calculations for Manhattan distance, empty Columns, empty Rows
dM = lambda r0,c0,r1,c1: np.abs(r0-r1) + np.abs(c0-c1)
dC = lambda c0,c1: np.sum( (min(c0,c1) < C) & (C < max(c0,c1)) )
dR = lambda r0,r1: np.sum( (min(r0,r1) < R) & (R < max(r0,r1)) )

# Find all galaxy pairs
galaxies = np.argwhere(matrix == 1)
galaxy_pairs = list(combinations(galaxies, 2))

part_1 = np.sum( [ dM(r0,c0,r1,c1) + dC(c0,c1) + dR(r0,r1) for (r0,c0), (r1,c1) in galaxy_pairs ] )
part_2 = np.sum( [ dM(r0,c0,r1,c1) + dC(c0,c1) * (1000000-1) + dR(r0,r1) * (1000000-1) for (r0,c0), (r1,c1) in galaxy_pairs ] )

print("Part 1", part_1)
print("Part 2", part_2)
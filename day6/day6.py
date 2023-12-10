import math
from functools import reduce

def solve(A, B, C):
	D = B**2 - 4 * A * C
	x1 = (-B + math.sqrt(D)) / (2*A)
	x2 = (-B - math.sqrt(D)) / (2*A)
	delta = int(x2-0.01) - int(x1+0.01)
	return delta


lines = open("input.txt").read().splitlines()

times, distances = [ [ int(word) for word in line.split() if word.isnumeric() ] for line in lines ]

part1 = reduce(lambda x, y: x*y, [ solve(-1, t, -d) for t, d in zip(times, distances) ])

time = int("".join(map(str,times)))
distance = int("".join(map(str,distances)))

part2 = solve(-1, time, -distance)

print("Part 1:", part1)
print("Part 2:", part2)
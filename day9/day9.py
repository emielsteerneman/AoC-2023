import numpy as np

lines = open("input.txt").read().splitlines()

matrix = np.array( [ [ int(word) for word in line.split() ] for line in lines ] )

get_next_pt1 = lambda line: line[-1] + (0 if (diff := np.diff(line))[-1] == 0 else get_next_pt1(diff))
part1 = sum(map(get_next_pt1, matrix))
print("Part 1:", part1)
	
get_next_pt2 = lambda line: line[0] - (0 if (diff := np.diff(line))[-1] == 0 else get_next_pt2(diff))
part2 = sum(map(get_next_pt2, matrix))
print("Part 2:", part2)
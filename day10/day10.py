import numpy as np
import re

def matrix_to_string(matrix):
	return "\n".join([ "".join([ c for c in row ]) for row in matrix])

def string_to_matrix(string):
	tubes = [ list(_) for _ in string.splitlines() ]
	tubes = [ ['.'] + tube + ['.'] for tube in tubes]
	tubes = [['.'] * len(tubes[0])] + tubes + [['.'] * len(tubes[0])]
	matrix = np.array(tubes)
	return matrix

def get_surrounding(matrix, row, col):
	surrounding = [
		[(row-1, col), matrix[(row-1, col)]],
		[(row, col+1), matrix[(row, col+1)]],
		[(row+1, col), matrix[(row+1, col)]],
		[(row, col-1), matrix[(row, col-1)]],
	]

	connections = mapping[matrix[(row, col)]]
	connected_to = [ s for i, s in enumerate(surrounding) if connections[i]]
	connected_from = [ v for v,i in zip(surrounding,range(4)) if mapping[v[1]][(i+2)%4] ]
	surrounding = set([ s[0] for s in connected_to ])  & set([ s[0] for s in connected_from ])

	return surrounding

def dijkstra(matrix):
	row, col = np.argwhere(matrix == "S")[0]	
	explored = {(row, col):0}
	to_explore = [(row, col)]

	while len(to_explore):
		at = to_explore.pop(0)
		cost = explored[(at)]
		neighbours = get_surrounding(matrix, *at)
		for coord in neighbours:
			if coord not in explored: to_explore.append(coord)
			if coord not in explored: explored[coord] = cost + 1
			if(cost + 1 < explored[coord]):
				explored[coord] = min(explored[coord], cost+1)

	return explored

mapping = {
	'|': np.array([1,0,1,0]),
	'-': np.array([0,1,0,1]),
	'L': np.array([1,1,0,0]),
	'J': np.array([1,0,0,1]),
	'7': np.array([0,0,1,1]),
	'F': np.array([0,1,1,0]),
	'.': np.array([0,0,0,0]),
	'S': np.array([1,1,1,1]),
}

matrix = string_to_matrix(open("input.txt").read())

print("Part 1:", max(dijkstra(matrix).values()))

matrix_clean = np.full(matrix.shape, '.')
for at, _ in dijkstra(matrix).items(): matrix_clean[at] = matrix[at]

string_clean = matrix_to_string(matrix_clean)

string_clean = string_clean.replace("-", '')
string_clean = string_clean.replace("FJ", "|")
string_clean = string_clean.replace("L7", "|")
string_clean = string_clean.replace("F7", "")
string_clean = string_clean.replace("LJ", "")
string_clean = string_clean.replace("||", "")

lines = string_clean.split("\n")

total = 0

for line in lines:
	for i, c in enumerate(line):
		if c != ".": continue
		total += line[:i].count("|") % 2

print("Part 2:", total)
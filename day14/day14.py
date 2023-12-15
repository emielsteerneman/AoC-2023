import numpy as np
from time import time

file = open("input.txt").read()

hash_grid = lambda grid: hash(grid.data.tobytes())
total_load = lambda grid: sum( [ (i+1) * sum(row == 'O') for i, row in enumerate(grid[::-1]) ] )

def print_grid(grid):
	print()
	print(hash_grid(grid))
	print("\n".join([ "".join(_) for _ in grid  ]))

grid = np.array(list(map(list, file.splitlines())))
print_grid(grid)

# for i in range(0, len(grid)-1):
# 	i = len(grid)-i-1
# 	for ic in range(len(grid[i])):
# 		if grid[i][ic] == 'O' and grid[i-1][ic] == ".":
# 			grid[i][ic], grid[i-1][ic] = grid[i-1][ic], grid[i][ic]

# print_grid(grid)
p = lambda _ : " ".join(map(str, _))

def roll_grid(grid):
	index = -1 * (grid[0] == '.') + 1
	for i, row in enumerate(grid):
		if i == 0: continue
		cols_to_modify = (row == 'O') & (index != i)
		grid[ index[cols_to_modify.nonzero()], cols_to_modify.nonzero() ] = 'O'
		grid[i][ cols_to_modify ] = '.'
		index[ cols_to_modify ] += 1
		index[ row != '.' ] = i + 1

roll_grid((grid_part1 := np.copy(grid)))
print( total_load(grid_part1) )

print("===part2")
cache = {}
period = 0
history = []
h = hash_grid(grid)

tstart = time()
troll = 0
tload = 0
thash = 0
tdict = 0

for i in range(1000000000):
	ta = time()
	for w in range(4):
		roll_grid(grid)
		grid = np.rot90(grid, -1)
	troll += time() - ta

	ta = time()
	history.append( total_load( grid ) )
	tload += time() - ta

	# print_grid(grid)
	# print("Looking at", i)

	ta = time()
	h = hash_grid(grid)
	thash += time() - ta

	if h in cache:
		period = i - cache[h]
		print("Period:", period)
		print("Remaining:", (1000000000-i)%period)
		history_idx = i-period+((1000000000-i)%period)-1
		print("Get history at", i-period+((1000000000-i)%period))
		print("=", history[history_idx])
		break
	ta = time()
	if h not in cache: cache[h] = i
	tdict += time() - ta

print("Total", time()-tstart)
print("Troll", troll)
print("Tload", tload)
print("Thash", thash)
print("Thash", tdict)


# 89089
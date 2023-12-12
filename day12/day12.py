from functools import cache
import time

file = open("input.txt").read()

def get_springs(pattern):
	must     = tuple([c == '#' for c in pattern])
	must_not = tuple([c == '.' for c in pattern])
	return tuple([must, must_not])

def get_ints(pattern):
	return tuple(map(int, pattern.split(",")))

def parse(file, part2=False):
	springs_nums = [ line.split(" ") for line in file.splitlines() ]

	if not part2:
		springs_nums = [ (get_springs(s), get_ints(w)) for s, w in springs_nums]
	else:
		springs_nums = [ (get_springs("?".join([s]*5)), get_ints(",".join([w]*5))) for s, w in springs_nums ]
	return springs_nums

def find(arr, val):
	for i, v in enumerate(arr):
		if v == val:
			return i
	return len(arr)

@cache
def place_on_patterns(pattern, nums):
	must, must_not = pattern
	sum_must, sum_must_not, sum_nums = sum(must), sum(must_not), sum(nums)

	# Break if there are less numbers than spots to fill
	if sum_nums < sum_must: return 0

	# Return if there is nothing more to do
	if sum_must == 0 and len(nums) == 0: return 1

	n = nums[0]
	total = 0

	i = -1
	next_must = find(must, True)
	to = min(len(must) - sum_nums - len(nums) + 1, next_must)
	while i < to:
		i += 1
		
		if i+n < len(must) and must[i+n]: continue

		stop, x = False, i
		while x < i+n and not stop:
			stop = must_not[x]
			x += 1
		if stop: 
			i = x - 1
			continue

		total += place_on_patterns( (must[i+n+1:], must_not[i+n+1:]), nums[1:])

	return total

part1 = sum(place_on_patterns(*_) for _ in parse(file, part2=False))
part2 = sum(place_on_patterns(*_) for _ in parse(file, part2=True))

print("Part 1:", part1)
print("Part 2:", part2)
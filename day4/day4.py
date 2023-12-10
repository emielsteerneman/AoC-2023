import re
import time

get_ints = lambda line: [ int(num) for num in line.split() if num.isdigit()]

lines = open("input.txt").read().splitlines()

a_b = [ map(get_ints, line.split(":")[1].split("|")) for line in lines ]

n_matches = [ len(set(a) & set(b)) for a, b in a_b ]

part1 = sum([ 2 ** (n-1) for n in n_matches if 0 < n ])

n_cards = [1] * len(lines)

for i_n, n in enumerate(n_matches):
	for i in range(i_n + 1, i_n + 1 + n):
		n_cards[i] += n_cards[i_n]

part2 = sum(n_cards)

print("Part 1:", part1)
print("Part 2:", part2)
text = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

text = open("input.txt").read()

seeds = [ int(word) for word in text.splitlines()[0].split(" ") if word.isnumeric() ]

blocks = text.split("\n\n")[1:]

block_mappings = [ [ [ int(word) for word in line.split(" ") if word.isnumeric() ] for line in block.split("\n")[1:] ] for block in blocks ]
block_mappings = [ [ [ m[1], m[1]+m[2], m[0], m[0]+m[2] ] for m in mappings ] for mappings in block_mappings ]

min_destination = 999999999999999

# ------------------ a ------ <- N -> ------ b --------------------
ia, ib, iq, ir = 0, 1, 2, 3

for seed in seeds:
    at = seed
    for mappings in block_mappings:
        m = list(filter(lambda m: m[ia] < at < (m[ib]),  mappings))
        if len(m): at = at - m[0][ia] + m[0][iq]
    min_destination = min(min_destination, at)

print("Part 1:", min_destination)



def print_mappings(seeds, mappings):
	nmax = 100#max(map(lambda m: m[iA] + m[iN], mappings))

	ss = " " * nmax

	for iseed, seed in enumerate(seeds):
		if type(seed) is int : ss = ss[:seed-1] + str(iseed) + ss[seed:]
		else: ss = ss[:seed[0]] + (str(iseed) * (seed[1]-seed[0])) + ss[seed[1]:]

	s0 = "|    .    "*10
	s1 = "-" * nmax
	s2 = "-" * nmax

	for i, (A, B, Q, R) in enumerate(mappings):
		s1 = s1[:A] + (f'{i}'*(B-A)) + s1[B:]
		s2 = s2[:Q] + (f'{i}'*(R-Q)) + s2[R:]

	# print("#", mappings)
	print("_"*102)
	print("# "+ss)
	print("# "+s0)
	print("# "+s1)
	print("# "+s2)

# for mappings in block_mappings[:1]:
# 	print(mappings)
# 	print_mappings(seeds, mappings)	
# 	print()





seeds = list(zip(seeds[::2], seeds[1::2]))
seeds = [ [s[0], s[0]+s[1]] for s in seeds ]
print(seeds)

# for mappings in block_mappings[:1]:
# 	print(mappings)
# 	print_mappings(seeds, mappings)	
# 	print()

# print("###################################################################")

# seeds = [ [5,15], [34,38], [45,65] ]

# block_mappings = [[
# 	[10, 20, 13, 23],
# 	[30, 40, 33, 43],
# 	[50, 60, 53, 63],
# ]]

#
#
#
#
#
#
#
#

# for i in range(len(block_mappings[0])-1, -1, -1):
# 	A, B, Q, R = block_mappings[0][i]
# 	blocks_mappings[0] += [  ]

# print(block_mappings)

for block_mapping in block_mappings:
	print("\n\n\n\n\n\n\n")
	print("BEFORE", seeds)
	# print_mappings(seeds, block_mapping)

	# For each mapping
	seeds_new_outer = []
	for seed in seeds:
		print("\n\n\nSeed:", seed)
		seeds_current = [seed]
		for (A, B, Q, R) in block_mapping:
			# print_mappings(seeds_current, block_mapping)

			print(f"\n  Mapping: {A}-{B} | Seeds: {seeds_current}")
			seeds_new = []
			for rA, rB in seeds_current:
				print("    seed range:", f"{rA}-{rB}")

				# print_mappings([[rA, rB]], [(mB, mA, mN)])

				if rA < A:            print("      Case1") or seeds_new.append([ rA, min(rB, A) ])
				if B  < rB:           print("      Case2") or seeds_new.append([ max(rA, B), rB ])
				if rA < B and A < rB: print("      Case3") or seeds_new.append([ max(rA, A), min(rB, B) ])

				print("    seeds_new", seeds_new)
				# print_mappings(seeds_new, [(mB, mA, mN)])	
			seeds_current = seeds_new
		seeds_new_outer += seeds_current

	# print_mappings(seeds_new_outer, block_mapping)

	# Do the mapping

	# print(seeds_new_outer)

	seeds_next = []
	for rA, rB in seeds_new_outer:
		isMoved = False
		for (A, B, Q, R) in block_mapping:
			print(f"Mapping: {A}-{B} | Seed: {rA}-{rB}")
			if A <= rA and rB <= B: 
				print(f"MOVE IT -> {rA + (Q-A)}-{rB + (R-B)}")
				seeds_next += [[rA + (Q-A), rB + (R-B)]]
				isMoved = True
		if not isMoved:
			seeds_next += [ [rA, rB] ]
	seeds = seeds_next
	
	seeds = sorted(seeds, key=lambda s: s[0])

	print("AFTER", seeds)
	# print_mappings(seeds, block_mapping)

print(seeds[0][0])

"""
Cases:		-----rA------rB---------------
			-----------------A--------B---
			     [1      ]

			-------------rA-rB------------
			----------mA-------mB---------
                         [3 ]

			-----------------rA-------rB--
			-----mA------mB---------------
                             [2       ]

			-----rA---------rB------------
			----------mA-------mB---------
                 [1   ][3   ]

			-------------rA----------rB---
			----------mA-------mB---------
                         [3    ][2   ]

			-----rA------------------rB---
			----------mA-------mB---------
                 [1   ][3      ][2   ]


1: if rA < mA:             rA          to min(rB, mA)
2: if mB < rB:             max(rA,mB)  to rB
3: if rA < mB and mA < rB: max(rA, mA) to min(rB, mB)
"""
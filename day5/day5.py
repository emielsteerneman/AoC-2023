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

	print("_"*102)
	print("# "+ss)
	print("# "+s0)
	print("# "+s1)
	print("# "+s2)

text = open("input.txt").read()

seeds = [ int(word) for word in text.splitlines()[0].split(" ") if word.isnumeric() ]

blocks = text.split("\n\n")[1:]

# Convert [y, x, n] to [x, x+n, y, y+n]
block_mappings = [ [ [ int(word) for word in line.split() ] for line in block.split("\n")[1:] ] for block in blocks ]
block_mappings = [ [ [ m[1], m[1]+m[2], m[0], m[0]+m[2] ] for m in mappings ] for mappings in block_mappings ]

min_destination = 999999999999999

# Part 1
for seed in seeds:
    for mappings in block_mappings:										# Move seed through all the mappings
        m = list(filter(lambda m: m[0] < seed < (m[1]),  mappings))			# Check if any of the mappings in the current block apply to the seed
        if len(m): seed = seed - m[0][0] + m[0][2]							# If there is such a map, then apply it to the seed
    min_destination = min(min_destination, seed)							# Keep track of the lowest seed destination

print("Part 1:", min_destination)


# Part 2
# Convert seed list from [a, b, c, d, e, f] to [[a,b], [c,d], [e,f]]
seeds = list(zip(seeds[::2], seeds[1::2]))
# Convert seed list from [[a,b], [c,d], [e,f]] to [[a,a+b], [c,c+d], [e,e+f]]
seeds = [ [s[0], s[0]+s[1]] for s in seeds ]

# For each map
for block_mapping in block_mappings:
	seeds_new_outer = []
	# For each range of seeds
	for seed_range in seeds:
		seeds_current = [seed_range]
		for (A, B, Q, R) in block_mapping:
			seeds_new = []
			for rA, rB in seeds_current:
				if rA < A:            seeds_new.append([ rA, min(rB, A) ])
				if B  < rB:           seeds_new.append([ max(rA, B), rB ])
				if rA < B and A < rB: seeds_new.append([ max(rA, A), min(rB, B) ])
			seeds_current = seeds_new
		seeds_new_outer += seeds_current

	seeds_next = []
	for rA, rB in seeds_new_outer:
		isMoved = False
		for (A, B, Q, R) in block_mapping:
			if A <= rA and rB <= B: 
				seeds_next += [[rA + (Q-A), rB + (R-B)]]
				isMoved = True
		if not isMoved:
			seeds_next += [ [rA, rB] ]
	seeds = seeds_next
	
seeds = sorted(seeds, key=lambda s: s[0])
print("Part 2:", seeds[0][0])

"""
Cases:		-----rA------rB---------------
			-----------------A--------B---
			     [1      ]


			-------------rA-rB------------
			----------A--------B----------
                         [3 ]


			-----------------rA-------rB--
			-----A-------B----------------
                             [2       ]


			-----rA---------rB------------
			----------A--------B----------
                 [1   ][3   ]


			-------------rA----------rB---
			----------A--------B----------
                         [3    ][2   ]


			-----rA------------------rB---
			----------A--------B----------
                 [1   ][3      ][2   ]


1: if rA < A:            rA         to min(rB, A)
2: if B < rB:            max(rA,B)  to rB
3: if rA < B and A < rB: max(rA, A) to min(rB, B)
"""
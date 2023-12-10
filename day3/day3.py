import re

lines = open("input.txt").read().splitlines()
special = '/#=&+*$-@%'

def get_2d(lines, x1, y1, x2, y2):
	strings = []
	for y in range(max(0, y1), min(y2+1, len(lines))):
		substring = lines[y][max(x1,0):min(x2, len(lines[y]))]
		strings.append(substring)
	return "\n".join(strings), "".join(strings)

total1 = 0
total2 = 0
gears = {}

for iline, line in enumerate(lines):
	matches = [(m.start(0), m.end(0)) for m in re.finditer("\\d+", line)]
	if len(matches) == 0: continue

	for x1, x2 in matches:
		value = int(line[x1:x2])
		dx1, dy1, dx2, dy2 = max(x1-1,0), max(iline-1,0), min(x2+1,len(line)), min(iline+1,len(lines))
		box, string = get_2d(lines, dx1, dy1, dx2, dy2)
		
		adjacent = any([c in box for c in special])
		if adjacent: total1 += value

		if "*" in string:
			i = string.index("*")
			ax, ay = dx1 + (i%(dx2-dx1)), dy1 + i // (dx2-dx1)
			if (ax, ay) not in gears: gears[(ax, ay)] = []
			gears[(ax, ay)].append(value)

for values in gears.values():
	if len(values) == 2:
		total2 += values[0] * values[1]

print("Part 1:", total1)
print("Part 2:", total2)
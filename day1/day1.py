lines = open("input.txt").read().splitlines()

toInt = lambda line : int(line[0] + line[-1])
filterC = lambda line : [ c for c in line if c in "0123456789"]

# Part 1
total = sum([ toInt(filterC(line)) for line in lines ])
print("Part 1:", total)

# Part 2
mapping = [["one", "1"], ["two", "2"], ["three", "3"], ["four", "4"], ["five", "5"], ["six", "6"], ["seven", "7"], ["eight", "8"], ["nine", "9"]]

total = 0

for line in lines:
	for i in range(len(line)):
		for word, num in mapping:
			if line[i:].startswith(word):
				line = line[:i] + num + line[i+1:]

	total += toInt(filterC(line))

print("Part 2:", total)

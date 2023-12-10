lines = open("input.txt").read().splitlines()

print(lines[:3])

colors = ["red", "green", "blue"]

max_rgb = [ 12, 13, 14 ]

total1 = 0
total2 = 0

for line in lines:
	game, sets = line.split(":")
	game_id = int(game.split(" ")[1])
	sets = sets.strip().split(";")
	
	rgbs = []
	for s in sets:
		rgb = [0, 0, 0]
		dices_colors = [ dc.strip().split(" ") for dc in s.split(",")   ]
		for dice, color in dices_colors:
			rgb[colors.index(color)] += int(dice)
		rgbs.append(rgb)

	sets_correct = True
	highest = [0, 0, 0]

	for rgb in rgbs:
		for icolor, ncolor in enumerate(rgb):
			if(max_rgb[icolor] < ncolor):
				sets_correct = False
			if(highest[icolor] < ncolor):
				highest[icolor] = ncolor

	if sets_correct is True:
		total1 += game_id

	total2 += highest[0] * highest[1] * highest[2]

print("Day 1:", total1)
print("Day 2:", total2)

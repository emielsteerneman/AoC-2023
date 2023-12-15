from functools import reduce

instructions = open("input.txt").read().split(",")
make_hash = lambda s : reduce ( lambda h,c : (h+ord(c))*17 % 256, s, 0 )

print("Part 1:", sum(map(make_hash, instructions)))

boxes = [{} for _ in range(256)]

for instruction in instructions:
	if instruction.endswith("-"):
		label = instruction[:-1]
		box = boxes[make_hash(label)]
		if label in box: del box[label]
	else:
		label, fl = instruction[:-2], int(instruction[-1])
		boxes[make_hash(label)][label] = fl

print("Part 2:", sum([ sum([ (ibox+1) * (ilf+1) * lf for ilf, lf in enumerate(box.values()) ]) for ibox, box in enumerate(boxes) ]))
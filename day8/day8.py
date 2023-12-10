import heapq
import math

def input_to_graph_and_sequence():
    sequence, _, *graph = open("input.txt").read().splitlines()
    graph = { g[0:3] : (g[7:10], g[12:15]) for g in graph }
    sequence = [ "LR".index(c) for c in sequence ]
    return graph, sequence

def walk_until_end(graph, seq, at="AAA", part2=False):
    idx, steps = 0, 0
    while True:
        steps += 1
        at = graph[at][seq[idx]]
        idx = (idx + 1) % len(seq)
        if not part2 and at     == "ZZZ": return steps
        if     part2 and at[-1] ==   "Z": return steps
    return steps

graph, sequence = input_to_graph_and_sequence()

steps_part1 = walk_until_end(graph, sequence, "AAA")
print("Part 1:", steps_part1)

steps_part2 = [ walk_until_end(graph, sequence, at=g, part2=True) for g in graph if g[-1] == "A" ]
print("Part 2:", math.lcm(*steps_part2))
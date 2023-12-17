import numpy as np
from functools import reduce
from itertools import chain
from time import time

@profile
def change_direction(beam, mirror):
    (y, x), (dy, dx) = beam
    
    if mirror == ".": return [beam]
    if mirror == "/":  return [((y, x), (-dx, -dy))]
    if mirror == "\\": return [((y, x), ( dx,  dy))]
    if mirror == "-":
        if dy == 0: return [beam]
        if dx == 0: return [ ((y, x), (0, -1)), ((y, x), (0, 1)) ]
    if mirror == "|":
        if dy == 0: return [ ((y, x), (-1, 0)), ((y, x), (1, 0)) ]
        if dx == 0: return [beam]

file = open("input.txt").read()
grid = np.array([list(line) for line in file.splitlines()])

@profile
def get_activated(grid, beam):
    beams = [beam]
    tiles_activated = { beam }

    while len(beams):
        
        if not len(beams): break
        
        # Change direction of beams
        beams = chain(*[ change_direction(beam, grid[beam[0]]) for beam in beams ])
    
        # Move beams
        beams = [((y+dy, x+dx), (dy, dx)) for (y, x), (dy, dx) in beams]
        
        # Remove beams that have left the grid
        beams = [beam for beam in beams if beam[0][0] >= 0 and beam[0][0] < grid.shape[0] and beam[0][1] >= 0 and beam[0][1] < grid.shape[1]]   
        
        # Filter beams present in tiles_activated
        beams = { beam for beam in beams if beam not in tiles_activated }

        # Add beams to tiles_activated
        tiles_activated |= beams

    return len(set([yx for yx, _ in tiles_activated]))

print("Part 1:", get_activated(grid, ((0,0), (0,1))))
print("Part 2:", max(chain(*[ [get_activated(grid, ((0, i), (1, 0))), get_activated(grid, ((grid.shape[0]-1, i), (-1, 0))), get_activated(grid, ((i, 0), (0, 1))), get_activated(grid, ((i, grid.shape[1]-1), (0, -1)))] for i in range(grid.shape[0]) ])))

import numpy as np
import time

file = open("input.txt").read()
grid = np.array([ list(map(int, line)) for line in file.splitlines()])

def dijkstra(grid, min_straight=0, max_straight=3):
    
    def is_valid(y, x, dy, dx, nsteps):
        # If the path is out of bounds, cancel this path
        if y < 0 or grid.shape[0] <= y or x < 0 or grid.shape[1] <= x: return False
        # If we go through the beginning, cancel this path
        if y == 0 and x == 0: return False
        # Ensure that we can break 
        if y == grid.shape[0]-1 and x == grid.shape[1]-1 and nsteps <= min_straight: return False
        
        return True
    
    frontier = { (0, 0, 0, 1, 0), (0, 0, 1, 0, 0) }
    distance = {}
    distance[(0, 0, 0, 1)] = 0
    distance[(0, 0, 1, 0)] = 0

    visited = set()
    
    nodetokey = lambda node : (node[0], node[1], node[2], node[3])
    
    while 0 < len(frontier):
        # Sort the unvisited nodes by distance, so that the closest unvisited node can be selected first.
        at = y, x, dy, dx, nsteps = min(frontier, key = lambda node : distance[nodetokey(node)])
        cost = distance[nodetokey(at)]
        
        frontier.remove(at) 
        visited.add(at)

        # For the current node, consider all of its unvisited neighbors and calculate their tentative distances through the current node. 
        path_right = (y+dx, x-dy, dx, -dy, 1)
        path_straight = (y+dy, x+dx, dy, dx, nsteps+1)
        path_left = (y-dx, x+dy, -dx, dy, 1)
        
        if is_valid(*path_right) and min_straight < nsteps:
            y, x, dy, dx, _ = path_right
            if nodetokey(path_right) not in distance or cost + grid[y, x] < distance[nodetokey(path_right)]:
                distance[nodetokey(path_right)] = cost + grid[y, x]
            if path_right not in visited: frontier.add(path_right)
        
        if is_valid(*path_straight) and nsteps < max_straight:
            y, x, dy, dx, _ = path_straight
            if path_straight not in distance or cost + grid[y, x] < distance[nodetokey(path_straight)]:
                distance[nodetokey(path_straight)] = cost + grid[y, x]
            if path_straight not in visited: frontier.add(path_straight)
            
        if is_valid(*path_left) and min_straight < nsteps:
            y, x, dy, dx, _ = path_left
            if path_left not in distance or cost + grid[y, x] < distance[nodetokey(path_left)]:
                distance[nodetokey(path_left)] = cost + grid[y, x]
            if path_left not in visited: frontier.add(path_left)
    
    heats = []
    for node in distance:
        y, x, dy, dx = node
        if y == grid.shape[0]-1 and x == grid.shape[1]-1:
            heats.append(distance[node])
        
    return min(heats)
    
print("Part 1:", dijkstra(grid, 0, 3))
print("Part 2:", dijkstra(grid, 3, 10))
from collections import deque

GRID_DIM = 70 + 1 # adding one bc 0 based indexing 

with open("inputs/day18.txt", "r") as f:
    falling_bytes = [] 
    for i in f.read().split():
        x,y = i.split(",")
        falling_bytes.append((int(x), int(y)))

def simulate(num_iterations): 
    # BFS through GRID_DIM x GRID_DIM grid 
    q = deque([(0, 0, 0)]) # x, y, num_moves 
    visited = set()

    while q: 
        x, y, num_moves = q.popleft()
        if (x, y) in visited: 
            continue # skip rest of loop 
        visited.add((x, y))
        if x == GRID_DIM - 1 and y == GRID_DIM - 1: 
            return num_moves 
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_x, new_y = x + dx, y + dy
            if (
                # don't fall off the edge 
                0 <= new_x < GRID_DIM 
                and 0 <= new_y < GRID_DIM
                # valid move
                and (new_x, new_y) not in falling_bytes[:num_iterations]
            ):
                q.append((new_x, new_y, num_moves + 1))
    return -1 

part1 = simulate(1024)
print(f"Part 1: {part1}")


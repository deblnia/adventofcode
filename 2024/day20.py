from collections import deque

with open("inputs/day20.txt", "r") as f: 
    grid = f.read().splitlines()

NROWS = len(grid)
NCOLS = len(grid[0])

def find_start_end(grid):
    start = end = None
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'S':
                start = (i, j)
            elif grid[i][j] == 'E':
                end = (i, j)
    return start, end

def get_neighbors(pos):
    i, j = pos
    neighbors = []
    for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        new_i, new_j = i + di, j + dj

        if (0 <= new_i < NROWS and 
            0 <= new_j < NCOLS):
            neighbors.append((new_i, new_j))
    return neighbors

def bfs(grid, start):
    distances = {start: 0}
    queue = deque([start])
    
    while queue:
        current = queue.popleft()
        for next_pos in get_neighbors(current):
            if next_pos not in distances and grid[next_pos[0]][next_pos[1]] != '#':
                distances[next_pos] = distances[current] + 1
                queue.append(next_pos)
    
    return distances

def find_wall_cheats(grid):
    start, end = find_start_end(grid)
    
    # need distances from start and from end 
    forward_distances = bfs(grid, start)
    backward_distances = bfs(grid, end)
    
    normal_distance = forward_distances.get(end, float('inf'))
    
    savings = {}  # savings[i] = count_of_walls 
    for i in range(NROWS):
        for j in range(NCOLS):
            if grid[i][j] == '#':
                min_cheat_distance = float('inf')
                for before in get_neighbors((i, j)):
                    if before not in forward_distances:
                        continue
                    for after in get_neighbors((i, j)):
                        if after not in backward_distances:
                            continue
                        
                        cheat_distance = forward_distances[before] + 1 + backward_distances[after]
                        min_cheat_distance = min(min_cheat_distance, cheat_distance)
                
                if min_cheat_distance < normal_distance:
                    saved_time = normal_distance - min_cheat_distance
                    savings[saved_time] = savings.get(saved_time, 0) + 1
    
    return savings

savings = find_wall_cheats(grid)
p1 = sum(count for time_saved, count in savings.items() if time_saved > 100)
print(f"P1: {p1}")

def find_shortcuts(grid, max_cheat=20, min_savings=100):
    times = [[-1] * NCOLS for _ in range(NROWS)]
    
    # getting start and end 
    start = None
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val == 'S':
                start = (i, j)
                break
        if start:
            break
    
    # BFS
    queue = deque([start])
    times[start[0]][start[1]] = 0
    
    while queue:
        i, j = queue.popleft()
        current_time = times[i][j]

        for di, dj in [(0,1), (1,0), (0,-1), (-1,0)]:
            ni, nj = i + di, j + dj
            if (0 <= ni < NROWS and 0 <= nj < NCOLS and 
                (grid[ni][nj] == '.' or grid[ni][nj] == 'E') and
                (times[ni][nj] == -1 or current_time + 1 < times[ni][nj])):
                times[ni][nj] = current_time + 1
                if grid[ni][nj] == '.':
                    queue.append((ni, nj))
    
    # diamond pattern shortcut 
    shortcuts = set()
    
    for i in range(1, NROWS-1):
        for j in range(1, NCOLS-1):
            if grid[i][j] != '#':
                for radius in range(max_cheat + 1):
                    for di in range(radius + 1):
                        dj = radius - di
                        for si, sj in [(1,1), (1,-1), (-1,1), (-1,-1)]:
                            ni, nj = i + di*si, j + dj*sj
                            if (0 <= ni < NROWS and 0 <= nj < NCOLS and
                                grid[ni][nj] in ('.', 'S') and
                                times[ni][nj] != -1 and  # ensure point is reachable
                                times[i][j] != -1 and    # ensure current point is reachable
                                times[i][j] - times[ni][nj] >= min_savings + radius): # only check if > min_savings 
                                shortcuts.add((i, j, ni, nj))
    
    return len(shortcuts)

p2 = find_shortcuts(grid)
print(f"P2: {p2}")
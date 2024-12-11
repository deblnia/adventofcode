import sys 

with open(sys.argv[1], 'r') as f: 
    data = f.read().strip().splitlines()
    grid = []
    for r in data:
        grid.append([int(x) for x in r])

def count_from_start(grid, y, x):
    result = set()

    def dfs(y, x, i):
        if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid) or grid[y][x] != i:
            return
        elif i == 9:
            result.add((y, x))
        else:
            dfs(y + 1, x, i + 1)
            dfs(y, x - 1, i + 1)
            dfs(y, x + 1, i + 1)
            dfs(y - 1, x, i + 1)
    dfs(y, x, 0)
    return len(result)

def part_one(grid):
    count = 0
    for j in range(len(grid)):
        for i in range(len(grid[0])):
            if grid[j][i] == 0:
                count += count_from_start(grid, j, i)
    return count

p1 = part_one(grid)
print(f"Part 1: {p1}")

def part_two(grid):
    count = 0
    
    def dfs(y, x, i, visited):
        if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid):
            return 0
        if grid[y][x] != i or (y, x) in visited:
            return 0
        if i == 9:
            return 1
        
        visited.add((y, x))
        
        count = (dfs(y + 1, x, i + 1, visited) +
                 dfs(y, x - 1, i + 1, visited) +
                 dfs(y, x + 1, i + 1, visited) +
                 dfs(y - 1, x, i + 1, visited))
        
        visited.remove((y, x))
        
        return count
    
    for j in range(len(grid)):
        for i in range(len(grid[0])):
            if grid[j][i] == 0:
                count += dfs(j, i, 0, set())
    
    return count

p2 = part_two(grid)
print(f"Part 2: {p2}")
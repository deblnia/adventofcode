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






p2 = ""
print(f"Part 2: {p2}")
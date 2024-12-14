from collections import defaultdict

with open("inputs/day12.txt", "r") as f:
    data = f.read().splitlines()
    G = [list(row) for row in data]

ROWS, COLS = len(G), len(G[0])
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def flood_fill(x, y, plant_type, visited):
    stack = [(x, y)]
    visited.add((x, y))
    area = 0
    perimeter = 0

    while stack:
        cx, cy = stack.pop()
        area += 1
        for dx, dy in DIRECTIONS:
            nx, ny = cx + dx, cy + dy
            # Check bounds
            if 0 <= nx < ROWS and 0 <= ny < COLS:
                if G[nx][ny] == plant_type and (nx, ny) not in visited:
                    stack.append((nx, ny))
                    visited.add((nx, ny))
                elif G[nx][ny] != plant_type:
                    perimeter += 1
            else:
                # Out of bounds counts in perimeter
                perimeter += 1
    return area, perimeter

def calc_sum_area_perimeter(grid):
    visited = set()
    total = 0

    for i in range(ROWS):
        for j in range(COLS):
            if (i, j) not in visited:
                plant_type = grid[i][j]
                area, perimeter = flood_fill(i, j, plant_type, visited)
                total += area * perimeter

    return total

p1 = calc_sum_area_perimeter(G)
print(f"Part 1: {p1}")

def get_corners(grid, i, j):
    m, n = len(grid), len(grid[0])
    
    def is_same(x, y, plant):
        return (
            0 <= x < m and 
            0 <= y < n and 
            grid[x][y] == plant
        )
    
    plant = grid[i][j]
    
    NW = is_same(i-1, j-1, plant)
    N = is_same(i-1, j, plant)
    NE = is_same(i-1, j+1, plant)
    W = is_same(i, j-1, plant)
    E = is_same(i, j+1, plant)
    SW = is_same(i+1, j-1, plant)
    S = is_same(i+1, j, plant)
    SE = is_same(i+1, j+1, plant)
    
    return sum([
        N and W and not NW,  # Northwest corner
        N and E and not NE,  # Northeast corner
        S and W and not SW,  # Southwest corner
        S and E and not SE,  # Southeast corner
        not (N or W),         # Top-left edge
        not (N or E),         # Top-right edge
        not (S or W),         # Bottom-left edge
        not (S or E)          # Bottom-right edge
    ])

def find_region(grid, i, j):
    m, n = len(grid), len(grid[0])
    plant = grid[i][j]
    region = set()
    queue = {(i, j)}
    
    while queue:
        x, y = queue.pop()
        region.add((x, y))
        
        for nx, ny in [(x-1, y), (x, y-1), (x+1, y), (x, y+1)]:
            if (0 <= nx < m and 
                0 <= ny < n and 
                grid[nx][ny] == plant and
                (nx, ny) not in region and
                (nx, ny) not in queue):
                queue.add((nx, ny))

    corners = sum(get_corners(grid, x, y) for x, y in region)
    
    return region, corners * len(region)

def calc_sum_area_perimeter(grid):
    m, n = len(grid), len(grid[0])
    total = 0
    visited = set()
    
    for i in range(m):
        for j in range(n):
            if (i, j) not in visited:
                region, cost = find_region(grid, i, j)
                total += cost
                visited |= region
    
    return total

p2 = calc_sum_area_perimeter(G)
print(f'Part 2: {p2}')
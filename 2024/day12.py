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
print(f"Total sum of area * perimeter: {p1}")
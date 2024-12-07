with open("inputs/day6.txt", "r") as file: 
    GRID = file.read().splitlines()

ROWS = len(GRID)
COLS = len(GRID[0])

def find_guard(grid): 
    rows = len(grid)
    cols = len(grid[0])

    for row in range(rows): 
        for col in range(cols): 
            if grid[row][col] == "^":
                return (row, col)

# heavy heavy assist from https://github.com/salt-die/Advent-of-Code/blob/main/2024/day_06.py
def patrol(oy=-1, ox=-1):
    seen = set()
    y, x = find_guard(GRID)
    dy, dx = -1, 0
    while True:
        if not (0 <= y < ROWS and 0 <= x < COLS):
            return len(seen) if oy == -1 else False
        if GRID[y][x] == "#" or (y == oy and x == ox):
            y -= dy
            x -= dx
            dy, dx = dx, -dy
        elif (y, x, dy, dx) in seen:
            return True
        else:
            if oy == -1:
                seen.add((y, x))
            else:
                seen.add((y, x, dy, dx))
            y += dy
            x += dx


def part_one():
    return patrol()


def part_two():
    sum = 0 
    for row in range(ROWS): 
        for col in range(COLS): 
            if GRID[row][col] == ".":
                sum += patrol(row, col)
    return sum


p1 = part_one()
p2 = part_two()

print(p1)
print(p2)
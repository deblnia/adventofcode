with open("inputs/day6.txt", "r") as file: 
    GRID = file.read().splitlines()

# heavy heavy assist from https://github.com/salt-die/Advent-of-Code/blob/main/2024/day_06.py
START = next(
    (y, x) for y, line in enumerate(GRID) for x, char in enumerate(line) if char == "^"
)
H = len(GRID)
W = len(GRID[0])


def patrol(oy=-1, ox=-1):
    seen = set()
    y, x = START
    dy, dx = -1, 0
    while True:
        if not (0 <= y < H and 0 <= x < W):
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
    return sum(patrol(y, x) for y in range(H) for x in range(W) if GRID[y][x] == ".")


p1 = part_one()
p2 = part_two()

print(p1)
print(p2)
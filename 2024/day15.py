import sys

with open("inputs/day15.txt", "r") as f: 
    grid_str, ins = f.read().split("\n\n")
    grid = [list(row) for row in grid_str.split("\n")]

ROWS = len(grid)
COLS = len(grid[0])

sx, sy = 0, 0
for i in range(ROWS):
    for j in range(COLS):
        if grid[i][j] == "@":
            sx, sy = i, j
            break
    else:
        continue
    break

move_map = {"<": (0, -1), "^": (-1, 0), ">": (0, 1), "v": (1, 0)}

for move in ins.strip().replace("\n", ""):  
    dx, dy = move_map[move]
    rr, cc = sx + dx, sy + dy 
    keep_moving = True

    while True:
        if grid[rr][cc] == "#":  
            keep_moving = False
            break
        if grid[rr][cc] == ".":  
            break
        if grid[rr][cc] == "O":  
            rr, cc = rr + dx, cc + dy
        else:
            raise ValueError(f"Unexpected grid value: {grid[rr][cc]}")

    if not keep_moving:
        continue

    grid[sx][sy] = "."  
    sx, sy = sx + dx, sy + dy     
    if grid[sx][sy] == "O":  
        grid[rr][cc] = "O"
    grid[sx][sy] = "@" 

p1 = sum(
    r * 100 + c for r, row in enumerate(grid) for c, val in enumerate(row) if val == "O"
)

print(f"P1: {p1}")

# roooough. heavily borrowed from https://gitlab.com/0xdf/aoc2024/-/blob/main/day15/day15.py?ref_type=heads
grid_map = {"#": "##", "O": "[]", ".": "..", "@": "@."}
with open("inputs/day15.txt", "r") as f:
    grid_str, moves = f.read().split("\n\n")
grid = []
for row in grid_str.splitlines():
    new_row = []
    for val in row:
        new_row.extend(grid_map[val])
    grid.append(new_row)

for r, row in enumerate(grid):
    for c, val in enumerate(row):
        if val == "@":
            break
    else:
        continue
    break

move_map = {"<": (0, -1), "^": (-1, 0), ">": (0, 1), "v": (1, 0)}
for move in moves.replace("\n", ""):
    dr, dc = move_map[move]
    keep_moving = True
    to_move = [(r, c)] # need to keep track of the starting
    i = 0
    while i < len(to_move):
        rr, cc = to_move[i]
        i += 1
        nr, nc = rr + dr, cc + dc
        if (nr, nc) in to_move:
            continue
        if grid[nr][nc] == "#":
            do_move = False
            break
        if grid[nr][nc] == ".":
            continue
        if grid[nr][nc] == "[":
            to_move.extend([(nr, nc), (nr, nc + 1)])
        elif grid[nr][nc] == "]":
            to_move.extend([(nr, nc), (nr, nc - 1)])
        else:
            assert False

    if not keep_moving:
        continue
    grid_copy = [list(row) for row in grid]
    r, c = r + dr, c + dc
    for rr, cc in to_move:
        grid[rr][cc] = "."
    for rr, cc in to_move:
        grid[rr + dr][cc + dc] = grid_copy[rr][cc]

p2 = sum(
    r * 100 + c for r, row in enumerate(grid) for c, val in enumerate(row) if val == "["
)
print(f"Part 2: {p2}")


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

for move in ins.strip():  
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
    grid[sx][sy] = "@"  # Update the new position with '@'

# Compute the result
p1 = sum(
    r * 100 + c for r, row in enumerate(grid) for c, val in enumerate(row) if val == "O"
)

print(f"P1: {p1}")





p2 = ""
print("P2: {p2}")
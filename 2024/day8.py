from collections import defaultdict

grid = []
with open("inputs/day8.txt", "r") as file:
    for line in file:
        grid.append(list(line.strip()))

ROWS = len(grid)
COLS = len(grid[0])

antennas = defaultdict(list) # frequency : [(coord, coord), (coord, coord)]
for row in range(ROWS):
    for col in range(COLS):
        char = grid[row][col]
        if char != '.':
            antennas[char].append((row, col))


antinodes = set()

for frequency, positions in antennas.items():
    for idx_a, (row_a, col_a) in enumerate(positions):
        for idx_b in range(idx_a + 1, len(positions)):
            row_b, col_b = positions[idx_b]

            row_dist = abs(row_a - row_b)
            col_dist = abs(col_a - col_b)

            if row_a > row_b:
                row_antinode1 = row_a + row_dist
                row_antinode2 = row_b - row_dist
            else:
                row_antinode1 = row_a - row_dist
                row_antinode2 = row_b + row_dist

            if col_a > col_b:
                col_antinode1 = col_a + col_dist
                col_antinode2 = col_b - col_dist
            else:
                col_antinode1 = col_a - col_dist
                col_antinode2 = col_b + col_dist

            if 0 <= row_antinode1 < ROWS and 0 <= col_antinode1 < COLS:
                antinodes.add((row_antinode1, col_antinode1))
            if 0 <= row_antinode2 < ROWS and 0 <= col_antinode2 < COLS:
                antinodes.add((row_antinode2, col_antinode2))

print(f"P1: {len(antinodes)}")
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

antinodes_p2 = set()

for frequency, antenna_positions in antennas.items():
    num_antennas = len(antenna_positions)
    for i in range(num_antennas - 1):
        start_x, start_y = antenna_positions[i]
        for j in range(i + 1, num_antennas):
            end_x, end_y = antenna_positions[j]

            direction_x, direction_y = start_x - end_x, start_y - end_y

            current_x, current_y = start_x, start_y
            while 0 <= current_x < COLS and 0 <= current_y < ROWS:
                antinodes_p2.add((current_y, current_x))
                current_x += direction_x
                current_y += direction_y

            current_x, current_y = end_x, end_y
            while 0 <= current_x < COLS and 0 <= current_y < ROWS:
                antinodes_p2.add((current_y, current_x))
                current_x -= direction_x
                current_y -= direction_y

print(f"P2: {len(antinodes_p2)}")
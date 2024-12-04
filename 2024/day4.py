def read_input():
    with open('inputs/day4.txt', 'r') as file:
        return file.read().splitlines()

data = read_input()
def count_xmas_occurrences(grid):
    rows, cols = len(grid), len(grid[0])
    count = 0
    count2 = 0 

    for r in range(rows):
        for c in range(cols):
            # Horizontal "XMAS" and "SAMX"
            if c + 3 < cols and grid[r][c:c+4] == ['X', 'M', 'A', 'S']:
                count += 1
            if c + 3 < cols and grid[r][c:c+4] == ['S', 'A', 'M', 'X']:
                count += 1
            
            # Vertical "XMAS" and "SAMX"
            if r + 3 < rows and all(grid[r+i][c] == word for i, word in enumerate("XMAS")):
                count += 1
            if r + 3 < rows and all(grid[r+i][c] == word for i, word in enumerate("SAMX")):
                count += 1
            
            # Diagonal (down-right) "XMAS" and "SAMX"
            if r + 3 < rows and c + 3 < cols and all(grid[r+i][c+i] == word for i, word in enumerate("XMAS")):
                count += 1
            if r + 3 < rows and c + 3 < cols and all(grid[r+i][c+i] == word for i, word in enumerate("SAMX")):
                count += 1
            
            # Diagonal (up-right) "XMAS" and "SAMX"
            if r - 3 >= 0 and c + 3 < cols and all(grid[r-i][c+i] == word for i, word in enumerate("XMAS")):
                count += 1
            if r - 3 >= 0 and c + 3 < cols and all(grid[r-i][c+i] == word for i, word in enumerate("SAMX")):
                count += 1
            
            # QUESTION 2 - assist from https://github.com/jonathanpaulson/AdventOfCode/blob/master/2024/4.py
            if r + 2 < rows and c + 2 < cols and grid[r][c] == 'M' and grid[r + 1][c + 1] == 'A' and grid[r + 2][c + 2] == 'S' and grid[r + 2][c] == 'M' and grid[r][c + 2] == 'S':
                count2 += 1
            if r + 2 < rows and c + 2 < cols and grid[r][c] == 'M' and grid[r + 1][c + 1] == 'A' and grid[r + 2][c + 2] == 'S' and grid[r + 2][c] == 'S' and grid[r][c + 2] == 'M':
                count2 += 1
            if r + 2 < rows and c + 2 < cols and grid[r][c] == 'S' and grid[r + 1][c + 1] == 'A' and grid[r + 2][c + 2] == 'M' and grid[r + 2][c] == 'M' and grid[r][c + 2] == 'S':
                count2 += 1
            if r + 2 < rows and c + 2 < cols and grid[r][c] == 'S' and grid[r + 1][c + 1] == 'A' and grid[r + 2][c + 2] == 'M' and grid[r + 2][c] == 'S' and grid[r][c + 2] == 'M':
                count2 += 1
    print(f"p1: {count}")
    print(f"p2: {count2}")

    return count
grid = [list(row) for row in data]
count_xmas_occurrences(grid)

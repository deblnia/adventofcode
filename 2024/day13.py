import re

# super helpful video: https://www.youtube.com/watch?v=aTeV8AVuyoY

with open("inputs/day13.txt", "r") as f: 
    data = f.read().split("\n\n")

def solve(puzzle:str) -> tuple[int]: 
    a1, a2 = tuple(map(int, re.findall(r"Button A: X\+(\d+), Y\+(\d+)", puzzle)[0]))
    b1, b2 = tuple(map(int, re.findall(r"Button B: X\+(\d+), Y\+(\d+)", puzzle)[0]))
    c1, c2 = tuple(map(int, re.findall(r"Prize: X=(\d+), Y=(\d+)", puzzle)[0]))

    # cramer's rule 
    x = ((c1 * b2) - (b1 * c2)) / ((a1 * b2) - (b1 * a2))
    y = ((a1 * c2) - (c1 * a2)) / ((a1 * b2) - (b1 * a2))

    if int(x) == x and int(y) == y:
        return tuple(map(int, (x, y)))
    return (0, 0)


p1 = 0 
for puzzle in data: 
    a, b = solve(puzzle)
    p1 += a * 3 + b # token cost 
print(f"P1: {p1}")
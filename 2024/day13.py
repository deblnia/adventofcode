import re

# super helpful video: https://www.youtube.com/watch?v=aTeV8AVuyoY

with open("inputs/day13.txt", "r") as f: 
    data = f.read().split("\n\n")

def solve(puzzle:str, offset:int = 0) -> tuple[int]: 
    a1, a2 = tuple(map(int, re.findall(r"Button A: X\+(\d+), Y\+(\d+)", puzzle)[0]))
    b1, b2 = tuple(map(int, re.findall(r"Button B: X\+(\d+), Y\+(\d+)", puzzle)[0]))
    c1, c2 = tuple(map(int, re.findall(r"Prize: X=(\d+), Y=(\d+)", puzzle)[0]))
    c1 += offset
    c2 += offset

    # cramer's rule 
    x = ((c1 * b2) - (b1 * c2)) / ((a1 * b2) - (b1 * a2))
    y = ((a1 * c2) - (c1 * a2)) / ((a1 * b2) - (b1 * a2))

    if int(x) == x and int(y) == y:
        return tuple(map(int, (x, y)))
    return (0, 0)


p1 = 0 
p2 = 0
for puzzle in data: 
    a, b = solve(puzzle)
    p1 += a * 3 + b # token cost 
    a2, b2 = solve(puzzle, offset=10000000000000)
    p2 += a2 * 3 + b2
print(f"P1: {p1}")
print(f"P2: {p2}")

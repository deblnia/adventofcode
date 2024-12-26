# literally no way I could have done this 
# basically trying to understand 0xdf's solution: 
# https://gitlab.com/0xdf/aoc2024/-/blob/main/day21/day21.py

with open("inputs/day21.txt", "r") as f:
    codes = list(map(str.strip, f.readlines()))





for code in codes: 
    p1 = 0
for code in codes:
    best_length = float("inf")
    best_length2 = float("inf")
    for path1 in keys_to_paths(num_pad_paths, code):
        best_length = min(best_length, get_length(path1, 2))
        best_length2 = min(best_length2, get_length(path1, 25))
    p1 += int(code[:-1]) * best_length

print(f"P1: {p1}")

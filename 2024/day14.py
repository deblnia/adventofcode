# absolutely could not get this: https://gitlab.com/0xdf/aoc2024/-/blob/main/day14/day14.py?ref_type=heads
import re
import math
import sys

WIDTH = 101 
HEIGHT = 103

def safey_score(robots: list[tuple[int]]) -> int:
    midx = WIDTH // 2
    midy = HEIGHT // 2
    q1 = q2 = q3 = q4 = 0
    for x, y in robots:
        if x < midx and y < midy:
            q1 += 1
        elif x > midx and y < midy:
            q2 += 1
        elif x < midx and y > midy:
            q3 += 1
        elif x > midx and y > midy:
            q4 += 1
    return q1 * q2 * q3 * q4

with open("inputs/day14.txt", "r") as f:
    lines = list(map(str.strip, f.readlines()))

robots = []
for line in lines:
    # p=0,4 v=3,-3
    x, y, dx, dy = tuple(map(int, re.findall(r"-?\d+", line)))
    robots.append((x, y, dx, dy))

part1_robots = []
for x, y, dx, dy in robots:
    xf = (x + (dx * 100)) % WIDTH
    yf = (y + (dy * 100)) % HEIGHT
    part1_robots.append((xf, yf))

part1 = safey_score(part1_robots)
print(f"Part 1: {part1}")

t = []
ss = []
min_score = 1e10
for i in range(10000):
    snap = []
    for x, y, dx, dy in robots:
        xf = (x + (dx * i)) % WIDTH
        yf = (y + (dy * i)) % HEIGHT
        snap.append((xf, yf))
    t.append(i)
    sss = safey_score(snap)
    ss.append(sss)
    if sss < min_score:
        best_snap = snap[:]
        min_score = sss
        best_frame = i

for y in range(HEIGHT):
    for x in range(WIDTH):
        if (x, y) in best_snap:
            print("#", end="")
        else:
            print(".", end="")
    print()

part2 = best_frame
print(f"Part 2: {part2}")

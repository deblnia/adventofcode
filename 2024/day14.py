import re
import math

with open("inputs/day14.txt", "r") as f:
    WIDTH, HEIGHT = 101, 103 
    lines = list(map(str.strip, f.readlines()))
    # WIDTH, HEIGHT = 11, 7 

p1 = ""
print(f"P1: {p1}")
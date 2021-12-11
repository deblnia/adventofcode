# this is a stack-based interview question 

from os import PRIO_PGRP


PAREN_PAIRS = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

lines = []
with open("./inputs/day10.txt") as f:
    for line in f.read().splitlines():
        lines.append(line)
    f.close()
        

# part 1 

PAREN_SCORES = {
    ")": 3, 
    "]": 57, 
    "}": 1197, 
    ">": 25137
}

partone = 0
for line in lines: 
    stack = []
    for c in line:
        if c in PAREN_PAIRS:
            stack.append(PAREN_PAIRS[c])
        elif c != stack.pop():
            partone += PAREN_SCORES[c]
            break

print(f'part 1: {partone}')

# part 2 

NEW_PAREN_SCORES = {
    ")": 1, 
    "]": 2, 
    "}": 3, 
    ">": 4
}

scores = []
for line in lines:
    stack = []
    for c in line:
        if c in PAREN_PAIRS:
            stack.append(PAREN_PAIRS[c])
        elif c != stack.pop():
            break
    else:
        score = 0
        for c in reversed(stack):
            score *= 5
            score += NEW_PAREN_SCORES[c]
        scores.append(score)
    scores.sort()



print(f'part 2: {scores[len(scores) // 2]}')

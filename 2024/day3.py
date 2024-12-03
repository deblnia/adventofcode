import re

def read_input():
    with open('inputs/day3.txt', 'r') as file:
        return file.read().splitlines()

data = read_input()

data_string = "\n".join(data)

# part 2 assist from: https://github.com/mebeim/aoc/blob/master/2024/solutions/day03.py

# matches = [(a, b, None, don't), (a, b, do, None) ... ]
matches = re.findall(r"mul\((\d+),\s*(\d+)\)|(do\(\))|(don't\(\))", data_string)

sum = 0
sum2 = 0
enabled = False
for a, b, do, dont in matches:
    # next is either enabled or disabled 
    if do or dont:
        # change enabled based on whether do is present or not  
        enabled = bool(do)
    else:
        x = int(a) * int(b)
        sum += x
        sum2 += x * enabled

print('Part 1:', sum)
print('Part 2:', sum2)
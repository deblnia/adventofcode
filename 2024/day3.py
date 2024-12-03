import re

def read_input():
    with open('inputs/day3.txt', 'r') as file:
        return file.read().splitlines()

data = read_input()

# QUESTION 1 
data_string = "\n".join(data)

matches = re.findall(r"mul\((\d+),\s*(\d+)\)|(do\(\))|(don't\(\))", data_string)

sum = 0
sum2 = 0
enabled = False
for a, b, do, dont in matches:
    if do or dont:
        enabled = bool(do)
    else:
        x = int(a) * int(b)
        sum += x
        sum2 += x * enabled

print('Part 1:', sum)
print('Part 2:', sum2)
import re
def read_input():
    with open('inputs/day3.txt', 'r') as file:
        return file.read().splitlines()

data = read_input()

# Join the list into a single string
data_string = "\n".join(data)

pattern = r"mul\((\d+),\s*(\d+)\)"
matches = re.findall(pattern, data_string)

sum = 0
for i in matches: 
    num1, num2 = i 
    num1 = int(num1)
    num2 = int(num2) 
    product = num1 * num2 
    sum += product
print(f"p1: {sum}")
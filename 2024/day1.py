def read_input():
    with open('inputs/day1.txt', 'r') as file:
        return file.read().splitlines()

data = read_input()

l = []
r = []

for item in data: 
    left, right = item.split()  #
    l.append(int(left))  
    r.append(int(right)) 


# QUESTION 1 
l.sort()
r.sort() 

sum = 0 
for pair in zip(l, r):
    a, b = pair 
    sum += abs(b - a)
print(sum )
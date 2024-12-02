from collections import Counter 

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
print(sum) 


# QUESTION 2 

rc = Counter(r) 

weighted_sum = 0 
for i in l: 
    if i in rc: 
        weighted_sum += i * rc[i]
    else: 
        weighted_sum += 0 
print(weighted_sum)
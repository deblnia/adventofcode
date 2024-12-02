def read_input():
    with open('inputs/day2.txt', 'r') as file:
        return file.read().splitlines()

data = read_input()

# heavy assist from https://github.com/jonathanpaulson/AdventOfCode/blob/master/2024/2.py
def is_good(line): 
    inc_or_dec = (line == sorted(line) or line == sorted(line, reverse=True))
    right_diff = True 
    for i in range(len(line) - 1): 
        diff = abs(line[i] - line[i + 1]) 
        if not 1 <= diff <= 3: 
            right_diff = False 
    return inc_or_dec and right_diff  

safe_reports_count = 0 
safe_reports_one_removed = 0 

for line in data:
    level = list(map(int, line.split()))
    if is_good(level): 
        safe_reports_count += 1
    
    good = False 
    for j in range(len(level)): 
        tmp = level[:j] + level[j + 1:]
        if is_good(tmp): 
            good = True 
    if good:
        safe_reports_one_removed += 1 
    

print(f"Total number of safe lines: {safe_reports_count}")
print(f"Total number of safe lines if you could remove one: {safe_reports_one_removed}")


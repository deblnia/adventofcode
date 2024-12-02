def read_input():
    with open('inputs/day2.txt', 'r') as file:
        return file.read().splitlines()

data = read_input()


# QUESTION 1 
def is_good(xs): 
    inc_or_dec = (xs == sorted(xs) or xs == sorted(xs, reverse=True))
    ok = True 
    for i in range(len(xs) - 1): 
        diff = abs(xs[i] - xs[i + 1]) 
        if not 1 <= diff <= 3: 
            ok = False 
    return inc_or_dec and ok  

safe_reports_count = 0 

for line in data:
    level = list(map(int, line.split()))
    if is_good(level): 
        safe_reports_count += 1 
    

print(f"Total number of safe lines: {safe_reports_count}")

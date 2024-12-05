from collections import defaultdict

with open('inputs/day5.txt', 'r') as file:
    data = file.read().splitlines()

# Split the rules and updates
rules_rn = True
rules = defaultdict(list)
updates = []

for line in data:
    if line == "":
        rules_rn = False
    elif rules_rn:
        k, v = line.split("|")
        rules[int(k)].append(int(v))
    else:
        updates.append(list(map(int, line.split(","))))  # Split into integers

def is_valid(update, rules):
    for start, ends in rules.items():
        for end in ends:
            if start in update and end in update:
                if update.index(start) > update.index(end):
                    return False
    return True

valid_updates = []
for update in updates:
    if is_valid(update, rules):
        valid_updates.append(update)

middle = [update[len(update) // 2] for update in valid_updates if len(update) > 0]
result = sum(middle)

print(result)
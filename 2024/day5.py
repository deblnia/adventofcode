from collections import defaultdict, deque

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

print(f"p1: {result}")

# fuck a topological sort honestly 
def order_update(update, rules):
    adjacency_list = defaultdict(list)
    in_degree = defaultdict(int)
    
    for start, ends in rules.items():
        for end in ends:
            if start in update and end in update:
                adjacency_list[start].append(end)
                in_degree[end] += 1
                in_degree[start] 
    
    queue = deque([node for node in update if in_degree[node] == 0])
    ordered = []
    
    while queue:
        current = queue.popleft()
        ordered.append(current)
        for neighbor in adjacency_list[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return ordered

invalid_updates = []
corrected_updates = []

for update in updates:
    if not is_valid(update, rules):
        invalid_updates.append(update)
        corrected_updates.append(order_update(update, rules))

middle = [update[len(update) // 2] for update in corrected_updates if len(update) > 0]
result = sum(middle)

print(f"p2: {result}")

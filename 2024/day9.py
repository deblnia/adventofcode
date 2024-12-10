with open('inputs/day9.txt', 'r') as file: 
    # list of ints 
    data = list(map(int, file.read().strip()))

# https://www.youtube.com/watch?v=5k8O1EloI5M super helpful 
disk = [] 
for i in range(0, len(data), 2): 
    disk.extend(data[i] * [i // 2])
    if i + 1 < len(data): 
        disk.extend(data[i + 1] * [-1])

empties = [i for i, val in enumerate(disk) if val == -1]

i = 0
while True: 
    while disk[-1] == -1: disk.pop()
    target = empties[i]
    if target >= len(disk): 
        break 
    disk[target] = disk.pop()
    i += 1 

part1 = sum(i * val for i, val in enumerate(disk))

print(f"Part 1: {part1}")
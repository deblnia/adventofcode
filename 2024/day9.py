with open('inputs/day9.txt', 'r') as file: 
    # list of ints 
    data = list(map(int, file.read().strip()))

# https://www.youtube.com/watch?v=5k8O1EloI5M super helpful 
disk = [] 
for i in range(0, len(data), 2):
    # appends multiple elements at once, could also use append and nest the for loop   
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

isfile = True
files = {}
spaces = []
ptr = 0
for i, size in enumerate(data):
    if isfile:
        files[i // 2] = (ptr, size)
    else:
        spaces.append((ptr, size))
    isfile = not isfile
    ptr += size

for fid in reversed(files):
    loc, file_size = files[fid]
    space_id = 0
    while space_id < len(spaces):
        space_loc, space_size = spaces[space_id]
        if space_loc > loc:
            break
        if space_size == file_size:
            files[fid] = (space_loc, file_size)
            spaces.pop(space_id)
            break
        if space_size > file_size:
            files[fid] = (space_loc, file_size)
            spaces[space_id] = (space_loc + file_size, space_size - file_size)
            break
        space_id += 1

part2 = 0
for fid, (loc, size) in files.items():
    for i in range(loc, loc + size):
        part2 += fid * i
print(f"Part 2: {part2}")

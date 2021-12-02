input = open("inputs/day2.txt")
input_stream = input.read()
split = input_stream.splitlines()
input.close()

fully_split = []

for i in split: 
    tokenized = i.split() 
    fully_split.append(tokenized)
    
flat_list = [item for sublist in fully_split for item in sublist]

# part 1 

h,v = 0, 0 

for i in range(len(flat_list)): 
    
    if flat_list[i] == 'forward':
        h += int(flat_list[i+1])

    elif flat_list[i] == 'up':
        v -= int(flat_list[i+1]) 

    elif flat_list[i] == 'down': 
        v += int(flat_list[i+1])
    
    else: 
        pass

print(f'part 1: {h*v}')

# part 2 

h,v, a = 0, 0, 0

for i in range(len(flat_list)): 
    
    if flat_list[i] == 'forward':
        h += int(flat_list[i+1])
        a += v * int(flat_list[i+1])

    elif flat_list[i] == 'up':
        v -= int(flat_list[i+1]) 

    elif flat_list[i] == 'down': 
        v += int(flat_list[i+1])
    
    else: 
        pass

print(f'part 2: {h*a}')

    
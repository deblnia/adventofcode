

with open('inputs/day11.txt', 'r') as f: 
    data = list(map(int, f.read().strip().split()))

def rules(num): 
    if num == 0:
        return [1]
    
    st_num = str(num)
    
    if len(st_num) % 2 == 0:
        l = int(st_num[:len(st_num) // 2])
        r = int(st_num[len(st_num) // 2:])
        return [l, r]
    
    return [num * 2024]   

def simulate_blinks(initial_numbers, num_blinks):
    current_numbers = initial_numbers.copy()
    
    for _ in range(num_blinks):
        next_numbers = []
        for num in current_numbers:
            next_numbers.extend(rules(num))
        
        current_numbers = next_numbers
    
    return len(current_numbers)

p1 = simulate_blinks(data, 25)

print(f"part 1: {p1}")

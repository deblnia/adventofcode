from functools import lru_cache
from collections import deque
import tqdm 

with open('inputs/day11.txt', 'r') as f:
    data = list(map(int, f.read().strip().split()))

@lru_cache(None)
def rules(num):
    if num == 0:
        return [1]
    
    st_num = str(num)
    if len(st_num) % 2 == 0:
        mid = len(st_num) // 2
        l = int(st_num[:mid])
        r = int(st_num[mid:])
        return [l, r]
    
    return [num * 2024]

def simulate_blinks(initial_numbers, num_blinks):
    current_numbers = deque(initial_numbers)  
    
    for _ in tqdm.tqdm(range(num_blinks)):
        next_numbers = deque()
        while current_numbers:
            num = current_numbers.popleft()
            next_numbers.extend(rules(num))
        
        current_numbers = next_numbers 
    
    return len(current_numbers)

p1 = simulate_blinks(data, 25)
print(f"part 1: {p1}")

p2 = simulate_blinks(data, 75)
print(f"part 2: {p2}")


# RAMA'S WAY - WAY BETTER ACTUALLY UNDERSTANDS WHAT'S GOING ON 
# import math
# from collections import Counter
# def get_input(path):
#     with open(path) as file:
#         return Counter(list(map(int, file.readline().split())))


# def blink(stones):
#     result = Counter()
#     for stone, count in stones.items():
#         if stone == 0:
#             result[1] += count
#         elif (digits := math.floor(math.log10(stone) + 1)) % 2 == 0:
#             mid = digits // 2
#             left = stone // 10**mid
#             right = stone % 10**mid
#             result[left] += count
#             result[right] += count
#         else:
#             new_stone = stone * 2024
#             result[new_stone] += count
#     return result


# if __name__ == "__main__":
#     stones = get_input("./inputs/day11.txt")
#     for i in range(75):
#         stones = blink(stones)
#         if i == 24:
#             print(f"After 25 blinks: {sum(count for count in stones.values())}")
#     print(f"After 75 blinks: {sum(count for count in stones.values())}")
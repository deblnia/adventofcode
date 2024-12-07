from itertools import product
from tqdm import tqdm

def get_input(path): 
    with open(path, "r") as file: 
        data = file.read()
    d = {}
    for i in data.splitlines(): 
        target, rest = i.split(":")
        rr = []
        for i in rest.split(" "):
            if i != "":
                rr.append(int(i))
        d[target] = rr
    return d

def try_all_ops(target:int, values:list, ops:list[str]):
    # generate all combos of ops for the number of gaps 
    for operations in product(ops, repeat=len(values)-1):
        start = values[0]
        for i, op in enumerate(operations):
            if op == '+':
                start += values[i+1]
            elif op == '*':
                start *= values[i+1]
            elif op == "||": 
                start = int(str(start) + str(values[i +1]))
        if start == target:
            return target
    return 0


if __name__ == "__main__": 
    total_part1 = 0
    total_part2 = 0

    data = get_input("inputs/day7.txt")

    for target, nums in tqdm(data.items()):
        goal = int(target)
        total_part1 += try_all_ops(goal, nums, ['+', '*'])
        total_part2 += try_all_ops(goal, nums, ['+', '*', '||'])

    print(f"Part 1: {total_part1}")
    print(f"Part 2: {total_part2}")
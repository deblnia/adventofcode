# reference: 
# https://www.youtube.com/watch?v=6t1dR_-U_zE

with open("inputs/day3.txt") as file:
    data = file.read()
    lines = data.strip().split("\n")

NUM_ROWS = len(lines)
NUM_COLS = len(lines[0])


goods = [[[] for _ in range(NUM_ROWS)] for _ in range(NUM_COLS)]


def is_symbol(i, j, num):
    if not (0 <= i < NUM_ROWS and 0 <= j < NUM_COLS):
        return False

    if lines[i][j] == "*":
        goods[i][j].append(num)
    return lines[i][j] != "." and not lines[i][j].isdigit()


ans = 0

for i, line in enumerate(lines):
    start = 0

    j = 0

    while j < NUM_COLS:
        start = j
        num = ""
        while j < NUM_ROWS and line[j].isdigit():
            num += line[j]
            j += 1

        if num == "":
            j += 1
            continue

        num = int(num)

        # Number ended, look around
        is_symbol(i, start-1, num) or is_symbol(i, j, num)

        for k in range(start-1, j+1):
            is_symbol(i-1, k, num) or is_symbol(i+1, k, num)
                # ans += num 
                # break 
# PART 2 
# for i in range(NUM_COLS):
#     for j in range(NUM_ROWS):
#         nums = goods[i][j]
#         if lines[i][j] == "*" and len(nums) == 2:
#             ans += nums[0] * nums[1]

print(ans)
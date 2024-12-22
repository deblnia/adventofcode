
with open("inputs/day19.txt", "r") as f:
    tmp = f.read().splitlines()
    patterns_tmp = tmp[0].split(",")
    patterns_given = [x.strip() for x in patterns_tmp]
    targets = [x for x in tmp[1:] if x != ""]

def backtrack(patterns, target, start_idx): 
    # match whole pattern
    if start_idx == len(target):
        return True 
    # if not, try all patterns 
    for pattern in patterns: 
        # fits in target, and at given position
        if (start_idx + len(pattern) <= len(target) and 
            target[start_idx:start_idx + len(pattern)] == pattern):
            # fit rest of target 
            if backtrack(patterns, target, start_idx + len(pattern)):
                return True 
    return False  

def count_achievable(patterns, targets): 
    count = 0

    for target in targets: 
        can_create = backtrack(patterns, target, 0)
        if can_create:
            count += 1 
    return count 


p1 = count_achievable(patterns_given, targets)
print(f"P1: {p1}")
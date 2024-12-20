import re
with open("inputs/day17.txt", "r") as f: 
    a,b, c, *program = list(map(int, re.findall(r"\d+", f.read())))

def eval(a: int, b: int = 0, c: int = 0) -> list[int]:
    def combo(val: int) -> int:
        assert val != 7, "Invalid combo value"
        if val <= 3:
            return val
        reg_map = {4: a, 5: b, 6: c}
        return reg_map[val]

    ans = []
    i = 0
    while i < len(program): 
        opcode = program[i]
        operand = program[i+1]
        match opcode: 
            case 0:  
                a = round(a // (2 ** combo(operand)))
            case 1: 
                b = b ^ operand
            case 2: 
                b = combo(operand) % 8
            case 3: 
                if a != 0: 
                    i = operand 
                    continue
            case 4:
                b = b ^ c 
            case 5: 
                ans.append(combo(operand) % 8)
            case 6: 
                b = round(a // (2 ** combo(operand)))
            case 7:
                c = round(a // (2 ** combo(operand)))
        i += 2
    return ans 

p1 = ",".join(map(str, eval(a,b,c)))
print(f"P1: {p1}")

# p1 = ",".join(map(str, eval(a,b,c)))
# print(f"P1: {p1}")
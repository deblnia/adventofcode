
with open("inputs/day13.txt", "r") as f: 
    data = f.read().split("\n")
    D = []
    machine = {}
    for i in data:
        if i.startswith('Button A:'):
            coords = i.split('Button A: ')[1].split(', ')
            machine['A'] = (
                int(coords[0].split('X+')[1]), 
                int(coords[1].split('Y+')[1])
            )
        elif i.startswith('Button B:'):
            coords = i.split('Button B: ')[1].split(', ')
            machine['B'] = (
                int(coords[0].split('X+')[1]), 
                int(coords[1].split('Y+')[1])
            )
        elif i.startswith('Prize:'):
            coords = i.split('Prize: ')[1].split(', ')
            machine['Prize'] = (
                int(coords[0].split('X=')[1]), 
                int(coords[1].split('Y=')[1])
            ) 
            D.append(machine)
            machine = {}

p1 = D
print(f"P1: {p1}")
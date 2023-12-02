file = open("inputs/day1.txt", "r")
inputs = []
for line in file.readlines():
    inputs.append(str(line))

p1 = 0
p2 = 0
for line in inputs:
  p1_digits = []
  p2_digits = []
  for i,c in enumerate(line):
    if c.isdigit():
      p1_digits.append(c)
      p2_digits.append(c)
    for d,val in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
        # starts with avoids the sharing letters problems 
      if line[i:].startswith(val):
        p2_digits.append(str(d+1))
  p1 += int(p1_digits[0]+p1_digits[-1])
  p2 += int(p2_digits[0]+p2_digits[-1])

print(p1)
print(p2)

input_file = "./inputs/day6.txt"

with open(input_file, "r") as f:
    lantern_fish = [] 
    for i in f.readlines():
        one_fish = i.split(",")
        lantern_fish.append(one_fish)
    # unnesting because of split 
    lantern_fish = [int(j) for i in lantern_fish for j in i]

# part 1 

post_day = lantern_fish
for day in range(0,80):
        for i in post_day: 
            if i == 0: 
                post_day.append(9)
        post_day = [7 if i == 0 else i for i in post_day]
        post_day = [i - 1 for i in post_day] 
print(len(post_day))


# part 2 

pop = list(map(lambda n: lantern_fish.count(n), range(9)))

for day in range(256):
    newpop = [0] * 9
    for i in range(8):
        newpop[i] = pop[i+1]
    newpop[6] += pop[0]
    newpop[8] = pop[0]
    pop = newpop

print(sum(pop))





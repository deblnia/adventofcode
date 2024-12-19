import heapq
# slightly better but still rough. owed mostly to https://gitlab.com/0xdf/aoc2024/-/blob/main/day16/day16.py?ref_type=heads
with open("inputs/day16.txt", "r") as f:
    data = list(map(str.strip, f.readlines()))

for r, row in enumerate(data):
    for c, val in enumerate(row):
        if val == "S":
            start = (r, c)
            break
    else:
        continue
    break
# the unpacking is nice here 
queue = [(0, *start, 0, 1, [start])]
seen = {(*start, 0, 1)}
p1 = None
best_cost = float("inf")
points = set()

# bfs'ing through the grid 
while queue:
    cost, r, c, dr, dc, path = heapq.heappop(queue)
    seen.add((r, c, dr, dc))
    if data[r][c] == "E":
        if not p1:
            p1 = cost
        if cost <= best_cost:
            best_cost = cost
            for point in path:
                points.add(point)
        else:
            break
    if data[r + dr][c + dc] != "#" and (r + dr, c + dc, dr, dc) not in seen:
        heapq.heappush(
            queue, (cost + 1, r + dr, c + dc, dr, dc, path + [(r + dr, c + dc)])
        )
    for ndr, ndc in [(-dc, dr), (dc, -dr)]:
        if (r, c, ndr, ndc) not in seen and data[r + ndr][c + ndc] != "#":
            heapq.heappush(queue, (cost + 1000, r, c, ndr, ndc, list(path)))

print(f"P1: {p1}")
print(f"P2: {len(points)}")
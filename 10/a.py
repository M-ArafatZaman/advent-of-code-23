import sys
from collections import deque

a = [i.strip() for i in sys.stdin.readlines()]
# [from, to]
pipes = {
    "|": ([0,-1], [0, 1]),
    "-": ([-1,0], [1, 0]),
    "L": ([0,-1], [1, 0]),
    "J": ([0,-1], [-1,0]),
    "7": ([0, 1], [-1,0]),
    "F": ([0, 1], [1, 0]),
    "S": ([0, 1], [0,-1], [-1,0], [1, 0])
}

sy, sx = -1, -1

for y in range(len(a)):
    for x in range(len(a[y])):
        if a[y][x] == "S": 
            sx, sy = x, y
            break
#([prev_x, prev_y], [curr_x, curr_y])
q = deque()
q.append(([None, None], [sx, sy]))
visited: list[list[bool]] = [[False for i in j] for j in a]
dist: list[list[int]] = [[None for i in j] for j in a]
loops = []
while len(q) > 0:
    prev, curr = q.popleft()
    if visited[curr[1]][curr[0]]: continue

    visited[curr[1]][curr[0]] = True

    if prev[0] == None and prev[1] == None:
        dist[curr[1]][curr[0]] = 0
    else:
        dist[curr[1]][curr[0]] = dist[prev[1]][prev[0]] + 1
    
    pipe = pipes.get(a[curr[1]][curr[0]], [])
    visit_count = 0
    for curr_dx, curr_dy in pipe:
        next_x, next_y = curr[0] + curr_dx, curr[1] + curr_dy
        if visited[next_y][next_x]: 
            visit_count += 1
            continue
        next_pipe = pipes.get(a[next_y][next_x], [])
        connects = False
        for next_dx, next_dy in next_pipe:
            if next_x + next_dx == curr[0] and next_y + next_dy == curr[1]: connects = True
        
        if connects: q.append((curr, [next_x, next_y]))
    if visit_count == 2: loops.append(dist[curr[1]][curr[0]]) 

print(max(loops))





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
north_pipes = ("|", "L", "J")

sy, sx = -1, -1

for y in range(len(a)):
    for x in range(len(a[y])):
        if a[y][x] == "S": 
            sx, sy = x, y
            break
#([prev_x, prev_y], [curr_x, curr_y])
# q is a list of states
q = deque()
q.append([[None, None], [sx, sy]])
visited: list[list[bool]] = [[False for i in j] for j in a]
dist: list[list[int]] = [[None for i in j] for j in a]
loops = []
while len(q) > 0:
    states = q.popleft()
    prev = states[-2]
    curr = states[-1]

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
        
        if connects: 
            new_states = list(states)
            new_states.append([next_x, next_y])
            q.append(new_states)
    if visit_count == 2: loops.append(states) 

new_grid = [["." for i in range(len(a[0]))] for j in range(len(a))]
# Copy grid
for states in loops:
    for c, r in states:
        if c == None or r == None: continue
        if a[r][c] == "S": continue
        new_grid[r][c] = a[r][c]
# Set start point to the right pipe
if new_grid[sy][sx+1] != "." and new_grid[sy+1][sx] != ".": # F
    new_grid[sy][sx] = "F"
elif new_grid[sy][sx-1] != "." and new_grid[sy+1][sx] != ".": # 7
    new_grid[sy][sx] = "7"
elif new_grid[sy-1][sx] != "." and new_grid[sy][sx-1] != ".": # J
    new_grid[sy][sx] = "J"
elif new_grid[sy-1][sx] != "." and new_grid[sy][sx+1] != ".": # L
    new_grid[sy][sx] = "L"

NORTH_FACING_PIPES = ["L", "J", "|"]
_in = False
in_count = 0
for r in range(len(new_grid)):
    _in = False
    for c in range(len(new_grid[0])):
        cell = new_grid[r][c]
        if cell in NORTH_FACING_PIPES:
            _in = not _in
        if cell == ".":
            in_count += 1 if _in else 0
print(in_count)
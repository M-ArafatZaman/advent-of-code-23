import sys
from collections import defaultdict

a = [i.strip() for i in sys.stdin.readlines()]
seeds = []
maps = defaultdict(list)
keys = []
curr = None
# Build map
for i in a:
    if i == "": continue
    
    if ":" in i:
        if "seeds" == i.split(":")[0]: seeds = [int(i.strip()) for i in i.split(":")[1].strip().split(" ")]

        else:
            curr = i.split(" ")[0].split("-")[-1]
            keys.append(curr)
    else:
        maps[curr].append([int(j) for j in i.split(" ")])
# Seed
low = 10e50
for seed in seeds:
    curr_val = seed
    for key in keys:
        for dest, source, r in maps[key]:
            if curr_val >= source and curr_val <= (source+r-1):
                curr_val = dest + (curr_val - source)
                break
    
    if curr_val < low:
        low = curr_val
print(low)


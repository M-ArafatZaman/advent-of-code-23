import sys
from collections import defaultdict

a = [i.strip() for i in sys.stdin.readlines()]
seed_pair = []
maps = defaultdict(list)
keys = []
curr = None
# Build map
for i in a:
    if i == "": continue
    
    if ":" in i:
        if "seeds" == i.split(":")[0]: 
            seed_pair = [int(i.strip()) for i in i.split(":")[1].strip().split(" ")]
            seed_pair = [(seed_pair[i], seed_pair[i+1]) for i in range(0, len(seed_pair), 2)]
        else:
            curr = i.split(" ")[0].split("-")[-1]
            keys.append(curr)
    else:
        maps[curr].append([int(j) for j in i.split(" ")])
# Map seed-range pairs to other-range pairs
sub_pairs = seed_pair
tmp_sub_pairs = []
new_sub_pairs = []
for key in keys:
    for dest, source, r in maps[key]:
        for ss, ll in sub_pairs:
            if ss >= source and (ss+ll-1) <= (source+r-1):
                new_sub_pairs.append((dest+(ss-source), ll))
            elif ss < source and (ss+ll-1) >= source and (ss+ll-1) <= (source+r-1):
                new_sub_pairs.append((dest, ss+ll-source+1))
                tmp_sub_pairs.append((ss, source-ss))
            elif ss >= source and ss <= (source+r-1) and (ss+ll-1) > (source+r-1):
                new_sub_pairs.append((dest+(ss-source), source+r-ss))
                tmp_sub_pairs.append((source+r, ss+ll-(source+r)))
            elif ss < source and (ss+ll-1) > (source+r-1):
                new_sub_pairs.append((dest, r))
                tmp_sub_pairs.append((ss, source-ss))
                tmp_sub_pairs.append((source+r, ss+ll-(source+r)))
            else:
                tmp_sub_pairs.append((ss, ll))
        sub_pairs = tmp_sub_pairs
        tmp_sub_pairs = []
    sub_pairs.extend(new_sub_pairs)
    new_sub_pairs = []
print(min(sub_pairs, key=lambda a: a[0])[0])

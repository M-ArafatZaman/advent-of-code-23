import sys
from itertools import accumulate

uni = [list(i.strip()) for i in sys.stdin.readlines()]

# expand cols
rows = []
for i in range(len(uni)):
    star = True
    for j in uni[i]:
        if j != ".": 
            star = False
            break
    if star: rows.append(i)
cols = []
for col in range(len(uni[0])):
    star = True
    for row in range(len(uni)):
        if uni[row][col] != ".":
            star = False
            break
    if star: cols.append(col) 

# Build grid length prefix
rows_prefix = [0] * len(uni)
cols_prefix = [0] * len(uni[0])
r_ptr = 0
for r in range(len(rows_prefix)):
    if r_ptr < len(rows) and rows[r_ptr] == r:
        rows_prefix[r] = 1 if r == 0 else 1 + rows_prefix[r-1]
        r_ptr += 1
    else:
        rows_prefix[r] = 0 if r == 0 else rows_prefix[r-1]
c_ptr = 0
for c in range(len(cols_prefix)):
    if c_ptr < len(cols) and cols[c_ptr] == c:
        cols_prefix[c] = 1 if c == 0 else 1 + cols_prefix[c-1]
        c_ptr += 1
    else:
        cols_prefix[c] = 0 if c == 0 else cols_prefix[c-1]

vertex = []
for r in range(len(uni)):
    for c in range(len(uni[0])):
        if uni[r][c] == "#":
            vertex.append([r, c])

expansion = 1000000
s = 0
for i in range(len(vertex)):
    r, c = vertex[i]
    for j in range(i+1, len(vertex)):
        r0, c0 = vertex[j]
        s += abs(r-r0) + abs(c-c0)
        s += (rows_prefix[max(r, r0)] - rows_prefix[min(r, r0)]) * (expansion-1)
        s += (cols_prefix[max(c, c0)] - cols_prefix[min(c, c0)]) * (expansion-1)

print(s)
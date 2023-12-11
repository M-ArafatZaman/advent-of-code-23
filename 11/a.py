import sys

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

# Expansion
for row in range(len(uni)):
    for col_ext in range(len(cols)):
        uni[row].insert(cols[col_ext]+col_ext, '.')
for row_ext in range(len(rows)):
    uni.insert(rows[row_ext]+row_ext, ["."]*len(uni[0]))

vertex = []
for r in range(len(uni)):
    for c in range(len(uni[0])):
        if uni[r][c] == "#":
            vertex.append([r, c])

s = 0
p = 0
for i in range(len(vertex)):
    r, c = vertex[i]
    for j in range(i+1, len(vertex)):
        r0, c0 = vertex[j]
        s += abs(r-r0) + abs(c-c0)
        p += 1

print(s)
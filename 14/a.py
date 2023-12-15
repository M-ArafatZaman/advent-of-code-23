import sys
grid = [list(i.strip()) for i in sys.stdin.readlines()]

bot_col_ptr = [0] * len(grid[0])

for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == "O":
            if r != bot_col_ptr[c]:
                grid[bot_col_ptr[c]][c] = "O"
                grid[r][c] = "."
            bot_col_ptr[c] += 1

        elif grid[r][c] == "#":
            bot_col_ptr[c] = r + 1

s = 0
for r in range(len(grid)):
    stones = 0
    for c in range(len(grid)):
        if grid[r][c] == "O":
            stones += 1
    s += (len(grid)-r) * stones

print(s)


import sys

m: list[list[str]] = [list(i.strip()) for i in sys.stdin.readlines()]

taken = [[False]*len(m[0]) for _ in range(len(m))]

def getNum(r, c, nums):
    if m[r][c] == "." or taken[r][c]: return
    
    start_ptr = c

    while start_ptr > 0 and m[r][start_ptr].isdigit():
        start_ptr -= 1

    if not m[r][start_ptr].isdigit(): start_ptr += 1

    num = ""
    while start_ptr < len(m[0]) and m[r][start_ptr].isdigit():
        num += m[r][start_ptr]
        taken[r][start_ptr] = True
        start_ptr += 1

    nums.append(int(num))

ratios = []
grid = {(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)}
for r in range(len(m)):
    for c in range(len(m[0])):
        nums = []
        if m[r][c] != "*": continue

        for dr, dc in grid:
            if (r + dr) >= 0 and (r + dr) < len(m) and (c+dc) >= 0 and (c+dc) < len(m[0]):
                getNum(r+dr, c+dc, nums)

        if len(nums) == 2:
            ratios.append(nums[0]*nums[1])

print(sum(ratios))
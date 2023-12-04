import sys

a = [i.strip() for i in sys.stdin.readlines()]

copies = {i:1 for i in range(len(a))}

for card in range(len(a)):
    win, my_num = [[int(j) for j in i.strip().split(" ") if j != ""] for i in a[card].split(":")[1].split("|")]

    curr = 0
    for n in my_num:
        if n in win:
            curr += 1

    for j in range(copies[card]):
        for i in range(card+1, card+curr+1):
            copies[i] += 1

s = 0
for i in copies:
    s += copies[i]
print(s)
    

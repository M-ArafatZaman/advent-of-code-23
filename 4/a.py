import sys

a = [i.strip() for i in sys.stdin.readlines()]

t = 0
for card in a:
    win, my_num = [[int(j) for j in i.strip().split(" ") if j != ""] for i in card.split(":")[1].split("|")]

    curr = 0
    for n in my_num:
        if n in win:
            if curr == 0: curr = 1
            else: curr *= 2

    t += curr

print(t)
    

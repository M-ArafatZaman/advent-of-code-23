import sys
from collections import defaultdict
from functools import cmp_to_key
a = [i.strip().split(" ") for i in sys.stdin.readlines()]
score = {'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7, 'T': 8, 'J': 9, 'Q': 10, 'K': 11, 'A': 12}
def card(s: str) -> int:
    d = defaultdict(int)
    for i in s: d[i] += 1
    one = 0
    two = 0
    three = 0
    for j in d:
        if d[j] == 5: return 7
        if d[j] == 4: return 6
        if d[j] == 3: three += 1
        if d[j] == 2: two += 1
        if d[j] == 1: one += 1

    if three == 1 and two == 1: return 5
    if three == 1 and one == 2: return 4
    if two == 2: return 3
    if two == 1 and one == 3: return 2
    return 1

def cmp(item1, item2):
    card1 = card(item1[0])
    card2 = card(item2[0])
    if card1 != card2: return card1 - card2
    else:
        p = 0
        while (item1[0][p] == item2[0][p]): p += 1
        return score[item1[0][p]] - score[item2[0][p]]

a.sort(key=cmp_to_key(cmp))

w = 0
for i in range(len(a)):
    w += int(a[i][1]) * (i+1)
print(w)
import sys
from collections import defaultdict
from functools import cmp_to_key
a = [i.strip().split(" ") for i in sys.stdin.readlines()]
score = {'J': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, 'T': 9, 'Q': 10, 'K': 11, 'A': 12}
def card(s: str) -> int:
    d = defaultdict(int)
    for i in s: d[i] += 1
    one = 0
    two = 0
    three = 0
    four = 0
    for j in d:
        if d[j] == 5: return 7  # five of a kind
        if d[j] == 4: four += 1
        if d[j] == 3: three += 1
        if d[j] == 2: two += 1
        if d[j] == 1: one += 1

    j_count = d["J"]
    if j_count == 4: return 7 # 5 of a kind
    if j_count == 3 and two == 1: return 7  # 5 of a kind
    if j_count == 3 and one == 2: return 6  # 4 of a kind
    if j_count == 2 and three == 1: return 7 # 5 of a kind
    if j_count == 2 and two == 2: return 6 # 4 of a kind
    if j_count == 2 and one == 3: return 4 # three of a kind
    if j_count == 1 and four == 1: return 7 # 5 of a kind
    if j_count == 1 and three == 1: return 6 # four of a kind
    if j_count == 1 and two == 2: return 5 # full house
    if j_count == 1 and two == 1: return 4 # three of a kind
    if j_count == 1 and one == 5: return 2 # one pair

    if four == 1: return 6 # Four of a kind
    if three == 1 and two == 1: return 5 # full house
    if three == 1 and one == 2: return 4 # three of a kind   
    if two == 2: return 3   # two pair
    if two == 1 and one == 3: return 2 # one pair
    return 1    # high card

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
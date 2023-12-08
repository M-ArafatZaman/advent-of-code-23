import sys

a = [i.strip() for i in sys.stdin.readlines()]
inst = a[0]
mp = {}
for i in range(2, len(a)):
    start, opt = [j.strip() for j in a[i].split("=")]
    b, c = [j.strip() for j in opt[1:-1].split(",")]
    mp[start] = {
        "L": b, "R": c
    }

curr = "AAA"
inst_ptr = 0
s = 0
while curr != "ZZZ":
    curr = mp[curr][inst[inst_ptr]]
    s += 1
    inst_ptr = (inst_ptr + 1) % len(inst)
print(s)
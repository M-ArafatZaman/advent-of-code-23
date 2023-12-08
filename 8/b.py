import sys

a = [i.strip() for i in sys.stdin.readlines()]
inst = a[0]
mp = {}
curr = []
for i in range(2, len(a)):
    start, opt = [j.strip() for j in a[i].split("=")]
    b, c = [j.strip() for j in opt[1:-1].split(",")]
    mp[start] = {
        "L": b, "R": c
    }
    if start[-1] == "A": curr.append(start)

periods = []
# Find period
for i in curr:
    loop = False
    next = i
    inst_ptr = 0
    s = 0
    while not loop:
        next = mp[next][inst[inst_ptr]]
        inst_ptr = (inst_ptr + 1) % len(inst)
        s += 1
        if next[-1] == "Z":
            loop = True

    periods.append(s)

# GCD
def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

def lcm(a, b):
    return int(abs(a*b)/gcd(a, b))

curr = periods[0]
for i in range(1, len(periods)):
    curr = lcm(curr, periods[i])

print(curr)

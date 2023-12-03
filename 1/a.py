import sys

def digits(s: str) -> int:
    first = None
    last = None
    for i in s:
        if i.isdigit():
            first = i if not first else first
            last = i

    return int(first+last)

a = [digits(i.strip()) for i in sys.stdin.readlines()]

print(sum(a))

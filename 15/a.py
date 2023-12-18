data = input().split(",")

def hsh(s) -> int:
    curr = 0
    for i in s:
        curr += ord(i)
        curr *= 17
        curr = curr % 256

    return curr

s = 0
for i in data:
    s += hsh(i)
print(s) 
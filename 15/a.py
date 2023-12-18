from functools import reduce
data = list(map(lambda s: reduce(lambda curr, v: (17*(curr+ord(v))) % 256, list(s), 0), input().split(",")))
print(sum(data))
import sys
from math import ceil, sqrt

a = [i.strip() for i in sys.stdin.readlines()]
time = int("".join([str(int(j)) for j in a[0].split(":")[1].strip().split(" ") if j != ""]))
dist = int("".join([str(int(j)) for j in a[1].split(":")[1].strip().split(" ") if j != ""]))

# s^2 - t*s + d => t+sqrt(t^2 - 4 * 1*d)/2
n = ceil( (time-sqrt((time**2)-(4*(dist+.00001))))/2 )
lowest, greatest = n, time-n
print(greatest-lowest+1)

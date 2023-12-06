import sys
from math import ceil, sqrt

a = [i.strip() for i in sys.stdin.readlines()]
time = [int(j) for j in a[0].split(":")[1].strip().split(" ") if j != ""]
dist = [int(j) for j in a[1].split(":")[1].strip().split(" ") if j != ""]

s = 1
for i in range(len(time)):
    # s^2 - t*s + d => t+sqrt(t^2 - 4 * 1*d)/2
    n = ceil( (time[i]-sqrt((time[i]**2)-(4*(dist[i]+.00001))))/2 )
    lowest, greatest = n, time[i]-n
    s *= (greatest-lowest+1)
print(s)
    
import sys

a = [i.strip() for i in sys.stdin.readlines()]
time = [int(j) for j in a[0].split(":")[1].strip().split(" ") if j != ""]
dist = [int(j) for j in a[1].split(":")[1].strip().split(" ") if j != ""]

s = 1
for i in range(len(time)):
    lt, gt = None, None
    low_speed, high_speed = 0, time[i]
    low_achieved_dist, high_achieved_dist = 0, 0
    while (low_achieved_dist <= dist[i] and low_speed <= time[i]) or (high_achieved_dist <= dist[i] and high_speed >= 0):
        low_achieved_dist = (time[i]-low_speed)*low_speed
        high_achieved_dist = (time[i]-high_speed)*high_speed
        if low_achieved_dist > dist[i] and not lt: lt = low_speed
        if high_achieved_dist > dist[i] and not gt: gt = high_speed
        low_speed += 1
        high_speed -= 1

    s *= (gt-lt+1)
print(s)
    
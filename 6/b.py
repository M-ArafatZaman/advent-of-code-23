import sys

a = [i.strip() for i in sys.stdin.readlines()]
time = int("".join([str(int(j)) for j in a[0].split(":")[1].strip().split(" ") if j != ""]))
dist = int("".join([str(int(j)) for j in a[1].split(":")[1].strip().split(" ") if j != ""]))

lt, gt = None, None
low_speed, high_speed = 0, time
low_achieved_dist, high_achieved_dist = 0, 0
while (low_achieved_dist <= dist and low_speed <= time) or (high_achieved_dist <= dist and high_speed >= 0):
    low_achieved_dist = (time-low_speed)*low_speed
    high_achieved_dist = (time-high_speed)*high_speed
    if low_achieved_dist > dist and not lt: lt = low_speed
    if high_achieved_dist > dist and not gt: gt = high_speed
    low_speed += 1
    high_speed -= 1
    
print(gt-lt+1)
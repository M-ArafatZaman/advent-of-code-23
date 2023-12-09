import sys
import numpy as np 

a = [[int(j) for j in i.strip().split(" ")] for i in sys.stdin.readlines()]

def get_diff_arr(arr):
    diff = np.zeros(len(arr)-1, dtype=np.int64)
    for i in range(len(diff)):
        diff[i] = arr[i+1] - arr[i]
    return diff

def is_zero(arr):
    for i in arr: 
        if i != 0: return False
    return True

s = 0
for hist in a:
    diffs = []
    diff_arr = get_diff_arr(hist)
    while not is_zero(diff_arr):
        diffs.append(diff_arr)
        diff_arr = get_diff_arr(diff_arr)
    curr = 0
    for i in range(len(diffs)-1, -1, -1):
        curr = diffs[i][0] - curr
    s += hist[0] - curr
print(s)



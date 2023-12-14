import sys
import numpy as np 

def find_points(pattern):
    prev = "".join(pattern[0])
    for row in range(1, len(pattern)):
        curr = "".join(pattern[row])
        if prev == curr:
            l = row - 1
            r = row
            equal = True
            while l >= 0 and r < len(pattern):
                if "".join(pattern[l]) != "".join(pattern[r]):
                    equal = False
                    break
                l -= 1
                r += 1
            if equal:
                return row
        prev = curr
    return None

def process(pattern):
    horizontal_line = find_points(pattern)
    vertical_line = find_points(np.array(pattern).T.tolist())
    if vertical_line:
        return vertical_line
    if horizontal_line:
        return 100 * horizontal_line

def main():
    stdin = [i.strip() for i in sys.stdin.readlines()]

    summary = 0
    curr_pattern = []
    for i in stdin:
        if i != "":
            curr_pattern.append(list(i))
        else:
            summary += process(curr_pattern)
            curr_pattern = []
    summary += process(curr_pattern)
    print(summary)

main()


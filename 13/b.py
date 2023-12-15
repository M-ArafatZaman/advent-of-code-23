import sys
import numpy as np

def is_one_off(str_a, str_b):
    if len(str_a) != len(str_b): return False
    count = 0
    for i in range(len(str_a)):
        if str_a[i] != str_b[i]: count += 1
    return True if count == 1 else False

def find_points(pattern):
    prev = "".join(pattern[0])
    for row in range(1, len(pattern)):
        curr = "".join(pattern[row])
        if prev == curr or is_one_off(prev, curr):
            l = row - 1
            r = row
            equal = True
            one_off = False
            while equal and l >= 0 and r < len(pattern):
                if not one_off and is_one_off("".join(pattern[l]), "".join(pattern[r])):
                    one_off = True
                elif "".join(pattern[l]) != "".join(pattern[r]):
                    equal = False
                l -= 1
                r += 1
            if equal and one_off:
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


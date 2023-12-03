import sys

DIGITS = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

def digits(s: str) -> int:
    first = None
    last = None
    for i in range(len(s)):
        if s[i].isdigit():
            first = s[i] if not first else first
            last = s[i]
        else:
            for d in DIGITS:
                if i+len(d) <= len(s) and s[i:i+len(d)] == d:
                    first = DIGITS[d] if not first else first
                    last = DIGITS[d]
                    
    return int(first+last)

a = [digits(i.strip()) for i in sys.stdin.readlines()]

print(sum(a))

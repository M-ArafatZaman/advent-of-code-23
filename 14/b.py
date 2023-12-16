import sys
from collections import defaultdict

def spin(g):
    col_ptr = [0] * len(g[0])

    for r in range(len(g)):
        for c in range(len(g[0])):
            if g[r][c] == "O":
                if r != col_ptr[c]:
                    g[col_ptr[c]][c] = "O"
                    g[r][c] = "."
                col_ptr[c] += 1

            elif g[r][c] == "#":
                col_ptr[c] = r + 1

def hash_grid(grid):
    score = 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == "O": score += (r*len(grid[0])) + c
    return score

def cycle(g):
    spin(g) # north
    g = list(map(list, list(zip(*g)))) # West
    spin(g) # west
    g = list(map(list, list(zip(*g)))) # North
    g = g[::-1] # south
    spin(g) # south
    g = g[::-1] # north
    g = [i[::-1] for i in g] # east to west
    g = list(map(list, list(zip(*g)))) # east
    spin(g)
    g = list(map(list, list(zip(*g)))) # north
    g = [i[::-1] for i in g] # west to east

    return g

def main():
    grid = [list(i.strip()) for i in sys.stdin.readlines()]
    
    """
    Find the period of rotations.
    I.e rotations after which the state returns back to a previous state
    """
    hashes = defaultdict(int)
    steps = 0
    prev = None
    h = None
    N = 1000000000
    for _ in range(N):
        grid = cycle(grid)
        steps += 1
        prev = h
        h = hash_grid(grid)
        if hashes[h] > 0:
            break
        hashes[h] = hashes[prev] + 1 if prev else 1

    period = hashes[prev] + 1 - hashes[h]
    #print(period, "cycles")
    n = (N - steps) // period

    for _ in range(N - steps - (n * period)):
        grid = cycle(grid)

    """Calculate the north support force"""
    s = 0
    for r in range(len(grid)):
        stones = 0
        for c in range(len(grid)):
            if grid[r][c] == "O":
                stones += 1
        s += (len(grid)-r) * stones

    print(s)

if __name__ == "__main__":
    main()


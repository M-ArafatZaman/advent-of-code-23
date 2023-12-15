import sys
from tqdm import trange

def spin(g):
    bot_col_ptr = [0] * len(g[0])

    for r in range(len(g)):
        for c in range(len(g[0])):
            if g[r][c] == "O":
                if r != bot_col_ptr[c]:
                    g[bot_col_ptr[c]][c] = "O"
                    g[r][c] = "."
                bot_col_ptr[c] += 1

            elif g[r][c] == "#":
                bot_col_ptr[c] = r + 1

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

    for _ in trange(1000000000):
        grid = cycle(grid)

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


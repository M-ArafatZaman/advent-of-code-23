import sys
from collections import deque 

# {(from): (to)}
mirror = {
    "/": {
        (0,1): (-1, 0),
        (0,-1): (1, 0),
        (1,0): (0, -1),
        (-1,0): (0, 1)
    },
    "\\": {
        (0,1): (1, 0),
        (0,-1): (-1, 0),
        (1,0): (0, 1),
        (-1,0): (0, -1)
    }
}

# {(from): [(to)]}
splitter = {
    "|": {
        (0,1): [(-1, 0), (1,0)],
        (0,-1): [(-1, 0), (1,0)],
        (1,0): [(1,0)],
        (-1,0): [(-1,0)]
    },
    "-": {
        (0,1): [(0,1)],
        (0,-1): [(0,-1)],
        (1,0): [(0,-1), (0,1)],
        (-1, 0): [(0,-1), (0,1)]
    }
}

def main():
    data = [list(i.strip()) for i in sys.stdin.readlines()]
    new_grid = [['.'] * len(data[0]) for _ in data]
    horz_visited = [[False] * len(data[0]) for _ in data]
    vert_visited = [[False] * len(data[0]) for _ in data]

    # ((r, c), (dr, dc))
    q = deque()
    q.append(((0,0), (0, 1)))

    is_within_bounds = lambda r, c: (r >= 0 and r < len(data) and c >= 0 and c < len(data[0]))

    while len(q) > 0:
        (r, c), (dr, dc) = q.popleft()
        dv = []
        # Check visited
        if data[r][c] != ".":
            if data[r][c] in mirror:
                # Horizontal movement
                if dr == 0 and vert_visited[r][c]: continue
            
                # Vertical movement
                if dc == 0 and horz_visited[r][c]: continue

            if data[r][c] in splitter:
                # Horizontal movement
                if dr == 0 and horz_visited[r][c]: continue
                # Vertical movement
                if dc == 0 and vert_visited[r][c]: continue

            if dr == 0:
                horz_visited[r][c] = True
            elif dc == 0:
                vert_visited[r][c] = True

        # Get next state
        if data[r][c] in mirror:
            dv.append(mirror[data[r][c]][(dr, dc)])
        elif data[r][c] in splitter:
            dv.extend(splitter[data[r][c]][(dr, dc)])
        else:
            dv.append((dr, dc))
        
        for _dr, _dc in dv:
            if is_within_bounds( r+_dr, c+_dc ): q.append(((r+_dr, c+_dc), (_dr, _dc)))

        new_grid[r][c] = "#"

    print(sum( [ sum([1 if j == "#" else 0 for j in i]) for i in new_grid ] ))



if __name__ == "__main__":
    main()
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
    is_within_bounds = lambda r, c: (r >= 0 and r < len(data) and c >= 0 and c < len(data[0]))

    starting_points = []
    # Vertical
    for r in range(len(data)):
        starting_points.append(((r,0), (0,1)))
        starting_points.append(((r,len(data[0])-1), (0,-1)))
    # Horizontal
    for c in range(len(data[0])):
        starting_points.append(((0,c), (1,0)))
        starting_points.append(((len(data)-1,c), (-1,0)))

    m = 0
    # Go through every starting points
    for (R, C), (DR, DC) in starting_points:
        visited = [[[] for _ in data[0]] for _ in data]
        # ((r, c), (dr, dc))
        q = deque()
        q.append(((R, C), (DR, DC)))

        path = set()

        while len(q) > 0:
            (r, c), (dr, dc) = q.popleft()
            dv = []
            # Check visited
            if data[r][c] != ".":
                if (dr, dc) in visited[r][c]: continue
                visited[r][c].append((dr, dc))

            # Add to path
            path.add((r, c))

            # Get next state
            if data[r][c] in mirror:
                dv.append(mirror[data[r][c]][(dr, dc)])
            elif data[r][c] in splitter:
                dv.extend(splitter[data[r][c]][(dr, dc)])
            else:
                dv.append((dr, dc))
            
            for _dr, _dc in dv:
                if is_within_bounds( r+_dr, c+_dc ): q.append(((r+_dr, c+_dc), (_dr, _dc)))
        
        m = max(m, len(path))

    print( m )


if __name__ == "__main__":
    main()
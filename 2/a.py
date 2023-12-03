import sys

a = [i.strip() for i in sys.stdin.readlines()]

CONF = {"red": 12, "green": 13, "blue": 14}

pos = []
for g in a:
    game, draws = g.split(":")
    draw = draws.split(";")
    ispos = True
    for rgbs in draw:
        for rgb in rgbs.strip().split(","):
            balls, color = rgb.strip().split(" ")
            balls = int(balls)
            if balls > CONF[color]: ispos = False
    if ispos: pos.append(int(game.split(" ")[1]))

print(sum(pos))

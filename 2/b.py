import sys

a = [i.strip() for i in sys.stdin.readlines()]

pos = []
for g in a:
    game, draws = g.split(":")
    draw = draws.split(";")
    
    red, green, blue = -1, -1, -1
    for rgbs in draw:
        for rgb in rgbs.strip().split(","):
            balls, color = rgb.strip().split(" ")
            balls = int(balls)

            if color == "blue" and balls > blue: blue = balls
            if color == "green" and balls > green: green = balls
            if color == "red" and balls > red: red = balls

    pos.append(red*green*blue)
        
print(sum(pos))

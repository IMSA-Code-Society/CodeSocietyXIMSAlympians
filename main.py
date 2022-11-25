from graphics import *


# Collision lines
# Structure:
# 0: point #1
# 1: point #2
# 2: normal
colliders = [
    [[0, 400], [500, 400], [0, -1]] # Ground
]

def main():
    win = GraphWin("Title", 500, 500, autoflush=False)

    # Ball physics variables
    ballAcc = [0, 0]
    ballVel = [0, 0]
    ballPos = [0, 0]

    # Ball rendering
    ball = Circle(Point(ballPos[0], ballPos[1]), 10)
    ball.setFill("red")
    ball.draw(win)

    # Render colliders
    for collider in colliders:
        lineP1 = collider[0]
        lineP2 = collider[1]
        lineN = collider[2]
        # Render collider line
        p1 = Point(lineP1[0], lineP1[1])
        p2 = Point(lineP2[0], lineP2[1])
        line = Line(p1, p2)
        line.setOutline("blue")
        line.draw(win)
        # Render collider normal
        avgX = (lineP1[0] + lineP2[0]) / 2
        avgY = (lineP1[1] + lineP2[1]) / 2
        p1 = Point(avgX, avgY)
        p2 = Point(avgX + lineN[0], avgY + lineN[1] * 20)
        line = Line(p1, p2)
        line.setOutline("green")
        line.draw(win)
    
    while True:
        # Update position
        ballPos = [ballPos[0] + ballVel[0], ballPos[1] + ballVel[1]]
        ball.move(ballVel[0], ballVel[1])

        # Press ESC to close window
        if win.checkKey() == "Escape":
            win.close()

        # Update frame (also keep framerate at 30 FPS)
        update(30)

main()
from collisions import *
from graphics import *
from math import *
from slingshot import *

# Config
ballRadius = 5
friction = -0.06

def main():
    win = GraphWin("Title", 1000, 500, autoflush=False)

    # Collision lines
    # Structure:
    # 0: point #1
    # 1: point #2
    # 2: normal force vector
    colliders = [
        [[0, 400], [win.width, 400], [0, -1.6]], # Ground
        [[0.000000001, 0], [0.000000001, 500], [-1.4, 0]],
        [[win.width - 0.000000001, 0], [win.width - 0.000000001, 500], [-1.4, 0]],
        [[500, 200], [700, 200], [0, -1.6]],
        [[700, 400], [700, 200], [-1.4, 0]],
        [[500, 200], [400, 100], [-1.8*cos(pi/4), -1.8*sin(pi/4)]]
    ]

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
    
    # Ball physics variables
    ballAcc = [0, 0.098]
    ballPos = [100, 350]
    ballPrevPos = ballPos
    drawSlingshot(ballPos[0], ballPos[1], win)

    # Ball rendering
    ball = Circle(Point(ballPos[0], ballPos[1]), ballRadius)
    ball.setFill("red")
    ball.draw(win)

    mouse = win.getMouse()
    velcoords = [mouse.getX(), mouse.getY()]
    ballVel = [0.2*-(velcoords[0] - ballPos[0]), 0.2*-(velcoords[1] - ballPos[1])]
    print(ballVel)

    while win.isOpen():
        # Reset gravity acceleration
        ballAcc = [0, 0.098]

        # Check if ball intersects any colliders
        for collider in colliders:
            p1 = collider[0]
            p2 = collider[1]
            # Subtract coords so that the ball is at (0, 0)
            adjPoint1 = [p1[0] - ballPos[0], p1[1] - ballPos[1]]
            adjPoint2 = [p2[0] - ballPos[0], p2[1] - ballPos[1]]
            if circleLineIntersection(adjPoint1, adjPoint2, ballRadius):
                # Transform velocity according to normal
                normal = collider[2]
                ballAcc = [0, 0] # Remove gravity when collided
                ballVel = [ballVel[0] + ballVel[0] * normal[0], ballVel[1] + ballVel[1] * normal[1]]
                ballPos = [ballPos[0] + ballVel[0], ballPos[1] + ballVel[1]]

        # Update velocity and position
        ballVel = [ballVel[0] + ballAcc[0], ballVel[1] + ballAcc[1]]
        ballPos = [ballPos[0] + ballVel[0], ballPos[1] + ballVel[1]]

        # Render ball
        ball.move(ballPos[0] - ballPrevPos[0], ballPos[1] - ballPrevPos[1])
        ballPrevPos = ballPos

        # Press ESC to close window
        if win.checkKey() == "Escape":
            win.close()

        # Update frame (also keep framerate at 60 FPS)
        update(60)

main()
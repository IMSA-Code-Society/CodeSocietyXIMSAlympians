from collisions import *
from graphics import *


# Config
ballRadius = 10


# Collision lines
# Structure:
# 0: point #1
# 1: point #2
# 2: normal
colliders = [
    [[0, 400], [500, 400], [-0.06, -1.6]] # Ground
]

def main():
    win = GraphWin("Title", 500, 500, autoflush=False)

    # Ball physics variables
    ballAcc = [0, 0.098]
    ballVel = [1, 0]
    ballPos = [0, 0]
    ballPrevPos = [0, 0]

    # Ball rendering
    ball = Circle(Point(ballPos[0], ballPos[1]), ballRadius)
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
    
    while True:
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
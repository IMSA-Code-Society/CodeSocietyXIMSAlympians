from collisions import *
from graphics import *
from math import *
from slingshot import *
from balltypes import *
from random import *

# Config
friction = -0.06
balls = []
fps = 120

# this code runs every iteration of the simulation, and moves the balls
# this is in a function so that it can be iterated for every ball in balls
def updates(ball, colliders):

    # Reset gravity acceleration
        ball.acc = [0, 5.88/fps]

        # Check if ball intersects any colliders
        for collider in colliders:
            p1 = collider[0]
            p2 = collider[1]
            # Subtract coords so that the ball is at (0, 0)
            adjPoint1 = [p1[0] - ball.pos[0], p1[1] - ball.pos[1]]
            adjPoint2 = [p2[0] - ball.pos[0], p2[1] - ball.pos[1]]
            if circleLineIntersection(adjPoint1, adjPoint2, ball.radius):
                # Transform velocity according to normal
                normal = collider[2]
                if(abs(normal[1]) >= 0.1 and abs(normal[0]) <= 0.1):
                    ball.acc = [0, 0] # Remove gravity when collided
                ball.vel = [ball.vel[0] + ball.vel[0] * normal[0], ball.vel[1] + ball.vel[1] * normal[1]]
                ball.pos = [ball.pos[0] + ball.vel[0], ball.pos[1] + ball.vel[1]]

        # Update velocity and position
        ball.vel = [ball.vel[0] + ball.acc[0], ball.vel[1] + ball.acc[1]]
        ball.pos = [ball.pos[0] + ball.vel[0], ball.pos[1] + ball.vel[1]]

        # Render ball
        ball.move(ball.pos[0] - ball.prevPos[0], ball.pos[1] - ball.prevPos[1])
        ball.prevPos = ball.pos

def main():
    win = GraphWin("Title", 1000, 500, autoflush=False)

    # Collision lines
    # Structure:
    # 0: point #1
    # 1: point #2
    # 2: normal force vector
    colliders = [
        [[0, 400], [win.width, 400], [-0.05, -1.6], 'f'], # Ground
        [[0.000000001, 0], [0.000000001, 500], [-1.4, 0], 'f'], # Left Border
        [[win.width - 0.000000001, 0], [win.width - 0.000000001, 500], [-1.4, 0], 'f'], # Right Border
        [[500, 200], [700, 200], [0, -1.6], 'b'],
        [[700, 400], [700, 200], [-1.4, 0], 'b'],
        [[500, 200], [400, 100], [-1.8*cos(pi/4), -1.8*sin(pi/4)], 'b']
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
    ballPos = [100, 360]
    ballVars = [{"acc" : [0, 5.88/fps], "vel" : [1, 0], "pos" : ballPos, "prevPos" : ballPos, "color" : "red", "radius": 10}, {"acc" : [0, 5.88/fps], "vel" : [1, 0], "pos" : ballPos, "prevPos" : ballPos, "color" : "yellow", "radius": 10}, {"acc" : [0, 5.88/fps], "vel" : [1, 0], "pos" : ballPos, "prevPos" : ballPos, "color" : "blue", "radius": 6}]
    drawSlingshot(ballPos[0], ballPos[1], win)

    # Creates ball and sets its velocity according to the slingshot
    ball = Ball(ballVars[randint(0, 2)], win)
    velCoords = slingMouse(win)
    ball.vel = [0.1*-(velCoords[0] - ballPos[0]), 0.1*-(velCoords[1] - ballPos[1])]

    balls.append(ball) # adds the ball to the array of balls for updating

    while win.isOpen():
        for ball in balls: # updates every ball in the system
            updates(ball, colliders)

        # Press ESC to close window
        if win.checkKey() == "Escape":
            win.close()

        # Ball click
        if (win.checkMouse()):
            newBalls = ball.click()
            if (newBalls):
                for newBall in newBalls:
                    newBall.canClick = False
                    balls.append(newBall)

        for b in balls:
            if (max(abs(b.vel[0]), abs(b.vel[1])) <= 0.5 and abs(b.acc[0]) <= 0.1 and b.pos[1] + b.radius >= 395) or abs(b.pos[0]-500)>500:
                b.removeBall()
                balls.remove(b)
                if len(balls) == 0:
                    ballVars = [{"acc" : [0, 5.88/fps], "vel" : [1, 0], "pos" : ballPos, "prevPos" : ballPos, "color" : "red", "radius": 10}, {"acc" : [0, 5.88/fps], "vel" : [1, 0], "pos" : ballPos, "prevPos" : ballPos, "color" : "yellow", "radius": 10}, {"acc" : [0, 5.88/fps], "vel" : [1, 0], "pos" : ballPos, "prevPos" : ballPos, "color" : "blue", "radius": 6}]
                    ball = Ball(ballVars[randint(0, 2)], win)
                    velcoords = slingMouse(win)
                    ball.vel = [0.1*-(velcoords[0] - ballPos[0]), 0.1*-(velcoords[1] - ballPos[1])]
                    balls.append(ball)
                    break

        # Update frame (also keep framerate at 720 FPS)
        update(fps)

main()
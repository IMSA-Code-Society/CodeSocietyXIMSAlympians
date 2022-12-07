from collisions import *
from graphics import *
from math import *
from slingshot import *
from balltypes import *
from random import *

# Config
friction = -0.06
balls = []
blocks = []
fps = 120

# this code runs every iteration of the simulation, and moves the balls
# this is in a function so that it can be iterated for every ball in balls
def updates(ball, colliders, win):

    # Reset gravity acceleration
        ball.acc = [0, 5.88/fps]

        # Check if ball intersects any colliders
        for collider in colliders:
            try:
                t = collider[3]
                p1 = collider[0]
                p2 = collider[1]
            except:
                t = 'b'
                p1 = collider.pos
                p2 = collider.pos2
            # Subtract coords so that the ball is at (0, 0)
            adjPoint1 = [p1[0] - ball.pos[0], p1[1] - ball.pos[1]]
            adjPoint2 = [p2[0] - ball.pos[0], p2[1] - ball.pos[1]]

            try:
                rad = ball.radius
            except:
                rad = max(abs(ball.pos2[0] - ball.pos[0]), abs(ball.pos2[1] - ball.pos[1]))

            if circleLineIntersection(adjPoint1, adjPoint2, rad):
                ball.canClick = False
                # Transform velocity according to normal
                try:
                    normal = collider[2]
                except:
                    normal = [collider.acc[0], -1*collider.acc[1]]
                    pass
                if(abs(normal[1]) >= 0.1 and abs(normal[0]) <= 0.1):
                    ball.acc = [0, 0] # Remove gravity when collided
                ball.vel = [ball.vel[0] + ball.vel[0] * normal[0], ball.vel[1] + ball.vel[1] * normal[1]]
                ball.pos = [ball.pos[0] + ball.vel[0], ball.pos[1] + ball.vel[1]]
                if t == 'b':
                    print(ball.pos)
                
                if(t == 'b'):
                    for item in win.items[:]:
                        if item.__class__.__name__ == "Line":
                            if item.p1.x == collider[0][0] and item.p2.y == collider[1][1]:
                                if ball.vel[0] >= 1:
                                    item.undraw()
                                    ball.vel[0] *= 0.5
                                else:
                                    ball.vel[0] *= -0.5
                    colliders.remove(collider)
                    win.update(fps)
        
        for block in blocks:
            if (True in circleBlockIntersection(ball, block)):
                blocks.remove(block)
                block.undraw()

        # Update velocity and position
        ball.vel = [ball.vel[0] + ball.acc[0], ball.vel[1] + ball.acc[1]]
        ball.pos = [ball.pos[0] + ball.vel[0], ball.pos[1] + ball.vel[1]]

        # Render ball
        ball.move(ball.pos[0] - ball.prevPos[0], ball.pos[1] - ball.prevPos[1])
        ball.prevPos = ball.pos

def main():
    win = GraphWin("Title", 1000, 500, autoflush=False)

    #Draws background
    grass = Rectangle(Point(0,400),Point(win.width,500))
    grass.setFill(color_rgb(19,133,16))
    grass.draw(win)
    sky = Polygon(Point(0,400),Point(win.width,400),Point(win.width,0),Point(0,0))
    sky.setFill(color_rgb(0,181,226))
    sky.draw(win)

    # Collision lines
    # Structure:
    # 0: point #1
    # 1: point #2
    # 2: normal force vector
    colliders = [
        [[0, 400], [win.width, 400], [friction, -1.5], 'f'], # Ground
        #[[0.000000001, -500], [0.000000001, 500], [-1.2, 0], 'f'], # Left Border
        #[[win.width - 0.000000001, -500], [win.width - 0.000000001, 500], [-1.2, 0], 'f'], # Right Border
        #[[500, 200], [700, 200], [0, -1.6], 'b'],
        #[[700, 400], [700, 200], [-1.4, 0], 'b'],
        #[[500, 200], [400, 100], [-1.8*cos(pi/4), -1.8*sin(pi/4)], 'b'],
        #[[400, 100], [400, 0], [-1.4, 0], 'b']
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
        if(collider[3] == 'b'):
            line.setOutline(color_rgb(153, 51, 0))
            line.setWidth(5);
        line.draw(win)
    
    
    # adds the blocks at the end that don't have gravity, but disappear when hit
    blocks.append(Block({"acc" : [0, 5.4], "vel" : [0, 0], "pos" : [420, 320], "pos2" : [430, 400], "prevPos" : [300, 200], "color" : "brown"}, win))
    blocks.append(Block({"acc" : [0, 5.4], "vel" : [0, 0], "pos" : [510, 320], "pos2" : [520, 400], "prevPos" : [300, 200], "color" : "brown"}, win))
    blocks.append(Block({"acc" : [0, 5.4], "vel" : [0, 0], "pos" : [520, 320], "pos2" : [420, 310], "prevPos" : [300, 200], "color" : "brown"}, win))

    blocks.append(Block({"acc" : [0, 5.4], "vel" : [0, 0], "pos" : [440, 310], "pos2" : [450, 230], "prevPos" : [300, 200], "color" : "brown"}, win))
    blocks.append(Block({"acc" : [0, 5.4], "vel" : [0, 0], "pos" : [490, 310], "pos2" : [500, 230], "prevPos" : [300, 200], "color" : "brown"}, win))
    blocks.append(Block({"acc" : [0, 5.4], "vel" : [0, 0], "pos" : [440, 240], "pos2" : [500, 230], "prevPos" : [300, 200], "color" : "brown"}, win))

    blocks.append(Block({"acc" : [0, 5.4], "vel" : [0, 0], "pos" : [460, 210], "pos2" : [480, 230], "prevPos" : [300, 200], "color" : "green"}, win))

    blocks.append(Block({"acc" : [0, 5.4], "vel" : [0, 0], "pos" : [820, 320], "pos2" : [830, 400], "prevPos" : [300, 200], "color" : "brown"}, win))
    blocks.append(Block({"acc" : [0, 5.4], "vel" : [0, 0], "pos" : [910, 320], "pos2" : [920, 400], "prevPos" : [300, 200], "color" : "brown"}, win))
    blocks.append(Block({"acc" : [0, 5.4], "vel" : [0, 0], "pos" : [820, 320], "pos2" : [920, 310], "prevPos" : [300, 200], "color" : "brown"}, win))

    blocks.append(Block({"acc" : [0, 5.4], "vel" : [0, 0], "pos" : [840, 310], "pos2" : [850, 230], "prevPos" : [300, 200], "color" : "brown"}, win))
    blocks.append(Block({"acc" : [0, 5.4], "vel" : [0, 0], "pos" : [890, 310], "pos2" : [900, 230], "prevPos" : [300, 200], "color" : "brown"}, win))
    blocks.append(Block({"acc" : [0, 5.4], "vel" : [0, 0], "pos" : [840, 240], "pos2" : [900, 230], "prevPos" : [300, 200], "color" : "brown"}, win))

    blocks.append(Block({"acc" : [0, 5.4], "vel" : [0, 0], "pos" : [860, 210], "pos2" : [880, 230], "prevPos" : [300, 200], "color" : "green"}, win))

    # Ball physics variables
    ballPos = [100, 360]
    ballVars = [{"acc" : [0, 5.88/fps], "vel" : [1, 0], "pos" : ballPos, "prevPos" : ballPos, "color" : "red", "radius": 10}, 
    {"acc" : [0, 5.88/fps], "vel" : [1, 0], "pos" : ballPos, "prevPos" : ballPos, "color" : "yellow", "radius": 10}, 
    {"acc" : [0, 5.88/fps], "vel" : [1, 0], "pos" : ballPos, "prevPos" : ballPos, "color" : "blue", "radius": 6},
    {"acc" : [0, 5.88/fps], "vel" : [1, 0], "pos" : ballPos, "prevPos" : ballPos, "color" : color_rgb(192,192,192), "radius": 12}]
    drawSlingshot(ballPos[0], ballPos[1], win)

    # Creates ball and sets its velocity according to the slingshot
    ball = Ball(ballVars[randint(0, 3)], win)
    velCoords = slingMouse(win)
    ball.vel = [0.1*-(velCoords[0] - ballPos[0]), 0.1*-(velCoords[1] - ballPos[1])]

    balls.append(ball) # adds the ball to the array of balls for updating


    while win.isOpen():
        for ball in balls: # updates every ball in the system
            updates(ball, colliders, win)

        #for block in blocks:
        #    updates(block, blocks, win)

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
            if (max(abs(b.vel[0]), abs(b.vel[1])) <= 0.5 and abs(b.acc[0]) <= 0.1 and b.pos[1] + b.radius >= colliders[0][0][1]-5) or abs(b.pos[0]-500)>500 or abs(b.pos[0]-500)<0:
                b.removeBall()
                balls.remove(b)
                if len(balls) == 0:
                    ballVars = [{"acc" : [0, 5.88/fps], "vel" : [1, 0], "pos" : ballPos, "prevPos" : ballPos, "color" : "red", "radius": 10}, {"acc" : [0, 5.88/fps], "vel" : [1, 0], "pos" : ballPos, "prevPos" : ballPos, "color" : "yellow", "radius": 10}, {"acc" : [0, 5.88/fps], "vel" : [1, 0], "pos" : ballPos, "prevPos" : ballPos, "color" : "blue", "radius": 6}, {"acc" : [0, 5.88/fps], "vel" : [1, 0], "pos" : ballPos, "prevPos" : ballPos, "color" : color_rgb(192,192,192), "radius": 10}]
                    ball = Ball(ballVars[randint(0, 3)], win)
                    velcoords = slingMouse(win)
                    ball.vel = [0.1*-(velcoords[0] - ballPos[0]), 0.1*-(velcoords[1] - ballPos[1])]
                    balls.append(ball)
                    break

        # Update frame (also keep framerate at constant FPS)
        update(fps)

        if len(blocks) == 0:
            for b in balls:
                b.removeBall()
            txt = Text(Point(win.width/2, win.height/2), 'You Win!')
            txt.setSize(35)
            txt.setFill('black')
            txt.draw(win)
            ex = Text(Point(win.width/2, 9*win.height/10), 'Click to close window')
            ex.setFill('black')
            ex.draw(win)
            win.getMouse()
            win.close()

main()
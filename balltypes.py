from graphics import *
from math import *

class Ball:

    def __init__(self, params, win):
        # unpacks the dictonary input and sets all fields equal to their initial values
        self.acc = params["acc"]
        self.vel = params["vel"]
        self.pos = params["pos"]
        self.prevPos = params["prevPos"]
        self.color = params["color"]
        self.radius = params["radius"]
        self.win = win
        self.canClick = True

        self.circle = Circle(Point(self.pos[0], self.pos[1]), self.radius)
        self.circle.setFill(self.color)
        self.circle.draw(self.win)

    def move(self, x, y): # the Ball move function uses the circle move function from Graphics.py
        self.circle.move(x, y)

    def click(self):
        if (self.canClick):
            self.canClick = False # so you can only click once
            v2 = self.vel[0]**2 + self.vel[1]**2

            if (self.color == "yellow"):
                if (v2 == 0):
                    self.vel[0] = 0
                else:
                    self.vel[0] += 5*(self.vel[0]/sqrt(v2))
                    self.vel[1] += 5*(self.vel[1]/sqrt(v2))
                
            if (self.color == "blue"): # creates two new balls, one above one below, and returns them to be added to the balls array
                return [Ball({"acc" : self.acc, "vel" : [self.vel[0] + 1*self.vel[1]/sqrt(v2), self.vel[1] - 1*self.vel[0]/sqrt(v2)], "pos" : self.pos, "prevPos" : self.pos, "color" : "blue", "radius": 6}, self.win),
                        Ball({"acc" : self.acc, "vel" : [self.vel[0] - 1*self.vel[1]/sqrt(v2), self.vel[1] + 1*self.vel[0]/sqrt(v2)], "pos" : self.pos, "prevPos" : self.pos, "color" : "blue", "radius": 6}, self.win)]
    def removeBall(self):
        print('yessir')
        self.circle.undraw()
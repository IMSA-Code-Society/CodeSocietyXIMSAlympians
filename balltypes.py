from graphics import *
from math import *

class Ball:

    def __init__(self, params, win):
        # Unpacks the dictionary input and sets all fields equal to their initial values
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

    def move(self, x, y): # The Ball move function uses the circle move function from Graphics.py
        self.circle.move(x, y)

    def click(self):
        if (self.canClick):
            self.canClick = False # So you can only click once
            v2 = self.vel[0] ** 2 + self.vel[1] ** 2

            if (self.color == "yellow"):
                if (v2 == 0):
                    self.vel[0] = 0
                else:
                    self.vel[0] += 5*(self.vel[0]/sqrt(v2))
                    self.vel[1] += 5*(self.vel[1]/sqrt(v2))
                
            if (self.color == "blue"): # Creates two new balls, one above one below, and returns them to be added to the balls array
                return [Ball({"acc" : self.acc, "vel" : [self.vel[0] + 1*self.vel[1]/sqrt(v2), self.vel[1] - 1*self.vel[0]/sqrt(v2)], "pos" : self.pos, "prevPos" : self.pos, "color" : "blue", "radius": 6}, self.win),
                        Ball({"acc" : self.acc, "vel" : [self.vel[0] - 1*self.vel[1]/sqrt(v2), self.vel[1] + 1*self.vel[0]/sqrt(v2)], "pos" : self.pos, "prevPos" : self.pos, "color" : "blue", "radius": 6}, self.win)]
    
            if(self.color == color_rgb(192,192,192)):
                #self.vel[1] = -self.vel[1]
                newBall = [Ball({"acc" : [0, self.acc[1]], "vel" : [0,0], "pos" : self.pos, "prevPos" : self.pos, "color" : color_rgb(192,192,192), "radius": 6}, self.win)]
                self.vel[0] *= 0.6
                self.vel[1] -= 3
                return newBall

    def removeBall(self):
        self.circle.undraw()

class Block():
    def __init__(self, params, win):
        # Unpacks the dictionary input and sets all fields equal to their initial values
        self.acc = params["acc"]
        self.vel = params["vel"]
        self.pos = params["pos"]
        self.pos2 = params["pos2"]
        self.prevPos = params["prevPos"]
        self.color = params["color"]
        self.win = win

        self.rect = Rectangle(Point(self.pos[0], self.pos[1]), Point(self.pos2[0], self.pos2[1]))
        self.rect.setFill(self.color)
        self.rect.draw(self.win)

    def move(self, x, y): # The Block move function uses the rect move function from Graphics.py
        self.rect.move(x, y)

    def undraw(self):
        self.rect.undraw()
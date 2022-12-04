from graphics import *

def drawSlingshot(bx, by, win):
    slingshot = Polygon(Point(bx - 15, by - 5), Point(bx - 10, by - 10), Point(bx, by + 10), Point(bx + 15, by - 5), Point(bx + 20, by), Point(bx, by + 50))
    slingshot.setFill('brown')
    slingshot.draw(win)

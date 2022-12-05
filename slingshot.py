from graphics import *

def drawSlingshot(bx, by, win):
    slingshot = Image(Point(bx, by), 'slingshot.png')
    slingshot.draw(win)

def slingMouse(win):
    start = win.checkMouse()
    mPos = [start.getX(), start.getY()]
    return mPos

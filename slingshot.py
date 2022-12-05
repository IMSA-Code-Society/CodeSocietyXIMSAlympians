from graphics import *

def drawSlingshot(bx, by, win):
    slingshot = Image(Point(bx, by), 'slingshot.png')
    slingshot.draw(win)

def slingMouse(win):
    start = win.checkMouse()
    mPos = [0, 0]
    while start == None:
        start = win.checkMouse()
        update(60)
    while start != None:
        mPos = [start.getX(), start.getY()]
        start = win.checkMouse() 
    return mPos

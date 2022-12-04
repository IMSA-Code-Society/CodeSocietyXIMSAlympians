from graphics import *

def drawSlingshot(bx, by, win):
    slingshot = Polygon(Point(bx - 15, by - 5), Point(bx - 10, by - 10), Point(bx, by + 10), Point(bx + 15, by - 5), Point(bx + 20, by), Point(bx, by + 50))
    slingshot = Polygon(Point(100, 100), Point(100, 100))
    slingshot = Image(Point(bx, by), 'AB2_Slingshot.png')
    # slingshot.setFill('brown')
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
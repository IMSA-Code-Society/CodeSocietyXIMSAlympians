from math import *


def checkSign(n):
    if n != 0:
        return abs(n)/n
    else:
        return n

def circleLineIntersection(p1, p2, r):
    # Check if circle intersects the segment
    # (By checking the signs, since point zero has to be in between a positive and a negative value)
    if checkSign(p1[0]) != checkSign(p2[0]) or checkSign(p1[1]) != checkSign(p2[1]):
        yIntercept = getYIntercept(p1, p2)
        # Check if y-intercept is radius away from the ball (which is at vector zero)
        return abs(yIntercept) <= r

def getYIntercept(p1, p2):
    slopeNumerator = p2[1] - p1[1]
    slopeDenominator = p2[0] - p1[0]
    # If slope is undefined
    if slopeDenominator == 0:
        return 0
    slope = slopeNumerator / slopeDenominator
    yIntercept = p1[1] - p1[0] * slope
    return yIntercept
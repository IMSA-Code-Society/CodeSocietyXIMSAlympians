from math import *

def checkSign(n):
    if n != 0:
        return abs(n)/n
    else:
        return n

def circleLineIntersection(p1, p2, r):
    # Source: https://mathworld.wolfram.com/Circle-LineIntersection.html
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    dr2 = dx ** 2 + dy ** 2
    D = p1[0] * p2[1] - p2[0] * p1[1]
    delta = r ** 2 * dr2 - D ** 2

    # Check if circle intersects the infinite line
    if delta >= 0:
        # Check if circle intersects the segment
        # (By checking the signs, since point zero has to be in between a positive and a negative value)
        if checkSign(p1[0]) != checkSign(p2[0]) or checkSign(p1[1]) != checkSign(p2[1]):
            return True

    return False
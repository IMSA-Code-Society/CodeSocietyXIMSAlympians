def circleLineIntersection(p1, p2, r):
    # Source: https://mathworld.wolfram.com/Circle-LineIntersection.html
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    dr2 = dx ** 2 + dy ** 2
    D = p1[0] * p2[1] - p2[0] * p1[1]
    delta = r ** 2 * dr2 - D ** 2

    if delta >= 0:
        return True
    else:
        return False
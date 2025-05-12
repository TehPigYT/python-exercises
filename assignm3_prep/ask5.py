import math


def distance(p1, p2):
    x, y = p1
    w, z = p2
    return math.sqrt((w - x) ** 2 + (z - y) ** 2)

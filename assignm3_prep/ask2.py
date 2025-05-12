from functools import partial


def trapezoid(b1, b2, h):
    return ((b1 + b2) * h) / 2


area1 = trapezoid(20, 15, 7.5)
print("Area 1:", area1)

trapezoid_fixed_bases = partial(trapezoid, 10, 5)
area2 = trapezoid_fixed_bases(8.9)
print("Area 2:", area2)

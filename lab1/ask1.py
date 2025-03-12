import math


def compute_result():
    a = 2**101
    b = math.pi**53
    c = 11**7

    res = math.sqrt(a / (b + c))

    print(res)

    string = str(res).replace(".", "")
    return string[:10]


print(compute_result())

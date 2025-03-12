import math
import re


def compute_factorial(num):
    sum = 0.0
    for i in range(num):
        sum += 1 / 2**i

    return sum


def input_number():
    while True:
        num = input("Enter a number: ")
        if not num.isdigit() or int(num) < 0:
            print("Input must be a number and positive")
        else:
            print(compute_factorial(int(num)))
            break


input_number()

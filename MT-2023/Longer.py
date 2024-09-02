"""Longer"""
import math
def main(r, a, b):
    """main"""
    circle = 2 * math.pi * r
    rectangle = (a * 2) + (b * 2)
    different = circle - rectangle
    different = abs(different)
    if circle > rectangle:
        print("Circle is longer")
        print(f"{different:.5f}")
    elif circle < rectangle:
        print("Rectangle is longer")
        print(f"{different:.5f}")
    else:
        print("Equal")
        print(f"{different:.5f}")
main(float(input()), float(input()), float(input()))

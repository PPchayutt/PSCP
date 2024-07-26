"""Math for IT"""
import math
def main():
    """main"""
    r = float(input())
    area = math.pi * r ** 2
    circumference = 2 * math.pi * r
    print(f"Area: {area:.3f}")
    print(f"Circumference: {circumference:.3f}")
main()

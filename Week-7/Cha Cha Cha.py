"""Cha Cha Cha"""
import math
def main():
    """main"""
    day = int(input())
    totalhour = 0
    for _ in range(day):
        if day <= 31:
            hour = float(input())
            hour = math.ceil(hour)
            if hour <= 24:
                totalhour += hour
    income = totalhour * 8720
    print(int(income))
main()

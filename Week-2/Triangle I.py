"""Triangle I"""
def main():
    """main"""
    side1 = float(input())
    side2 = float(input())
    side3 = float(input())
    if side1 > side2 and side1 > side3:
        sideC = side1
        sideA = side2
        sideB = side3
    elif side2 > side1 and side2 > side3:
        sideC = side2
        sideA = side1
        sideB = side3
    else:
        sideC = side3
        sideA = side1
        sideB = side2
    if abs(sideA**2 + sideB**2 - sideC**2) <= 0.01:
        print("Yes")
    else:
        print("No")
main()

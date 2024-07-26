"""Circular I"""
def main():
    """main"""
    x1 = float(input())
    y1 = float(input())
    r = float(input())
    x2 = float(input())
    y2 = float(input())
    a = (((x2 - x1)**2) + ((y2 - y1)**2))**0.5
    if a <= r:
        print("Yes")
    else:
        print("No")
main()

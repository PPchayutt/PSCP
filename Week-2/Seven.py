"""ONE TIME SEVEN"""
def main():
    """CALCULATE SEVEN"""
    x = int(input())
    remainder = x % 4
    if remainder == 1:
        print(7)
    elif remainder == 2:
        print(9)
    elif remainder == 3:
        print(3)
    else:
        print(1)
main()

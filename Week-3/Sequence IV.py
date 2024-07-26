"""Sequence IV"""
def main():
    """main"""
    x = int(input())
    y = 0
    for _ in range(x):
        for _ in range(1,x+1):
            y += 1
            print(y, end=" ")
        print()
main()

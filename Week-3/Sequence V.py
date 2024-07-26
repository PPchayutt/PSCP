"""Sequence V"""
def main():
    """main"""
    x = int(input())
    y = x
    for _ in range(x):
        for _ in range(1,8):
            if y > 0:
                print(y, end=" ")
            else:
                return
            y -= 1
        print()
main()

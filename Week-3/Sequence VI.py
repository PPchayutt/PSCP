"""Sequence VI"""
def main():
    """main"""
    x = int(input())
    for i in range(x):
        for j in range(x):
            if i>=j:
                print(j+1, end=" ")
            else:
                print(" ", end="")
        print()
main()

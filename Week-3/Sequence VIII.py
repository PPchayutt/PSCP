"""Sequence VIII"""
def main():
    """main"""
    x = int(input())
    for i in range(x):
        print(" " * (3 * (x - i - 1)), end="")
        for j in range(i+1):
            if i >= j:
                print(f"{j+1:>02}", end=" ")
            else:
                print("", end="")
        print()
main()

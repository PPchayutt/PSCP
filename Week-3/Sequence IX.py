"""Sequence IX"""
def main():
    """main"""
    num = int(input())
    for i in range(1, num + 1):
        for _ in range(num, i, -1):
            print("  ", end=" ")
        for j in range(1, i + 1):
            print(f"{j:02}", end=" ")
        for l in range(i - 1, 0, -1):
            print(f"{l:02}", end=" ")
        print()
main()

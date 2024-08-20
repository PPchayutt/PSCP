"""Sequence XI"""
def main(n):
    """main"""
    size = 2 * n - 1
    for i in range(size):
        for j in range(size):
            value = min(i, j, size - 1 - i, size - 1 - j) + 1
            print(f"{value:02d}", end=" ")
        print()
main(int(input()))

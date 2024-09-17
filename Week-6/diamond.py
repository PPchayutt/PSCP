"""diamond"""
def main(n):
    """main"""
    for i in range(n):
        spaces = " " * (n - i - 1)
        if i == 0:
            print(spaces + "*")
        elif i == n - 1:
            print("*" * n)
        else:
            stars = "*" + " " * (2 * i - 1) + "*"
            print(spaces + stars)
    for i in range(n - 2, -1, -1):
        spaces = " " * (n - i - 1)
        if i == 0:
            print(spaces + "*")
        else:
            stars = "*" + " " * (2 * i - 1) + "*"
            print(spaces + stars)
main(int(input()))

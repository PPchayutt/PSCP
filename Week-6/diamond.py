"""diamond"""
def main(n):
    """main"""
    for i in range(n // 2 + 1):
        spaces = " " * (n // 2 - i)
        if not i:
            print(spaces + "*")
        elif i == n // 2:
            print("*" * n)
        else:
            stars = "*" + " " * (2 * i - 1) + "*"
            print(spaces + stars)
    for i in range(n // 2 - 1, -1, -1):
        spaces = " " * (n // 2 - i)
        if not i:
            print(spaces + "*")
        else:
            stars = "*" + " " * (2 * i - 1) + "*"
            print(spaces + stars)
main(int(input()))

"""Parallelogram"""
def main(text):
    """main"""
    n = len(text)
    for i in range(1, n + 1):
        print(f"{' ' * (n - i)}{text[:i]}")
    for i in range(1, n):
        print(f"{text[i:]}")
main(input())

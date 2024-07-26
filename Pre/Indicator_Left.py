"""Indicator_Left"""
def main():
    """main"""
    k = int(input())
    n = int(input())
    for i in range(n):
        print(" " * abs(n // 2 - i)+ "*" * k)
main()

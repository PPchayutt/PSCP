"""Inflation"""
def main():
    """main"""
    n = int(float(input()) * 100)
    k = int(input())
    for _ in range(k):
        n += n*381//10000
    print(f"{n // 100}.{n % 100:>02}")
main()

"""Median"""
def main(n):
    """Median"""
    num = []
    for _ in range(n):
        num.append(float(input()))
        num.sort()
    if n % 2 == 1:
        median = num[n // 2]
    else:
        median = (num[n // 2] + num[(n // 2)-1])/2
    print(f"{median:.3f}")
main(int(input()))

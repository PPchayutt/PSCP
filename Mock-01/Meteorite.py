"""Meteorite"""
def main(a, b, c):
    """main"""
    count = 0
    asteroid_size = a
    while asteroid_size >= c:
        count += 1
        asteroid_size /= b
        if asteroid_size >= c:
            count += b - 1
    return count
a = float(input())
b = int(input())
c = float(input())
result = main(a, b, c)
print(result)

"""Home Run"""
def main(n, distance):
    """main"""
    count = 0
    for _ in range(n):
        field = float(input())
        if distance > field:
            count += 1
    print(count)
main(int(input()),float(input()))

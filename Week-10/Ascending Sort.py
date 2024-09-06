"""Ascending Sort"""
def main(times):
    """main"""
    number = []
    for _ in range(times):
        num = int(input())
        number.append(num)
    number.sort()
    for num in number:
        print(num)
main(int(input()))

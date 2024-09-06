"""Tuple's Sad life"""
def main():
    """main"""
    text = input().split()
    num = input()
    index = text.index(num)
    length  = text.count(num)
    for _ in range(length):
        for _ in range(length):
            print(index , end=" ")
        print()
main()

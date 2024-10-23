"""PickThemAgain"""
def main(num):
    """main"""
    count = 0
    for i in reversed(num):
        if not int(i) % 3 or not int(i) % 5:
            print(i)
            count += 1
    if not count:
        print("Nope")
main(input().split())

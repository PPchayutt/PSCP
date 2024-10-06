"""MissingNumber No Set"""
def main():
    """main"""
    lst = []
    count = int(input())
    while True:
        num = int(input())
        if not num:
            break
        lst.append(num)
    lst.sort()
    for i in range(1,count+1):
        if i not in lst:
            print(i)
main()

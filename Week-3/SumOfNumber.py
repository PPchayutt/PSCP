"""SumOfNumber"""
def main():
    """main"""
    neednum = int(input())
    if neednum == -1:
        total = 0
    else:
        num = 0
        total = 0
        while True:
            if total == neednum:
                break
            num = int(input())
            if num == -1:
                break
            num = abs(num)
            total += num
    print(total)
main()

"""GraderMachine"""
def main():
    """main"""
    start = int(input())
    stop = int(input())
    sums = 0
    num = ""
    if start < stop:
        while start <= stop:
            if not start % 2:
                num = num + ' ' + str(start)
                sums += start
            else:
                pass
            start += 1
    else:
        while start >= stop:
            if not start % 2:
                num = num + ' ' + str(start)
                sums += start
            else:
                pass
            start -=1
    print(f"pass :{num}")
    print(f"Sum : {sums}")
main()

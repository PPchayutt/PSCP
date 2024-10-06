'''GCD_v1'''
def main():
    '''doc'''
    firstnum = int(input())
    secnum = int(input())
    start = abs(max(firstnum,secnum))
    if start <= 2:
        print(start)
        return
    for i in range(start,0,-2):
        if not firstnum % i and not secnum % i:
            print(i)
            return
    print(1)
main()

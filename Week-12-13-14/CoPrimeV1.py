'''CoPrimeV1'''
def iscoprime(firstnum, secnum):
    '''doc'''
    start = abs(max(firstnum, secnum))
    returning = 1
    if 1 in (firstnum, secnum):
        returning = 1
        return returning
    for i in range(start,0,-1):
        if not firstnum % i and not secnum % i:
            returning = i
            break
    return returning
def main():
    '''doc'''
    firstnum = int(input())
    secnum = int(input())
    primy = iscoprime(firstnum, secnum)
    if primy == 1:
        print('YES')
        print(primy)
    else:
        print('NO')
        print(primy)
main()

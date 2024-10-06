'''All_Primes'''
import math
def is_prime(num):
    '''return true if prime'''
    if num <= 1:
        return False
    for i in range(2,int(math.sqrt(num))+1):
        if not num % i:
            return False
    return True
def main():
    """count prime"""
    num = int(input())
    total = 0
    for i in range(1, num+1):
        if is_prime(i):
            total += 1
    print(total)
main()

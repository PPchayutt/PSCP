"""isprime_large"""
import math
def is_prime(num):
    """return true if prime"""
    if num <= 1:
        return False
    for i in range(2,int(math.sqrt(num))+1):
        if not num % i:
            return False
    return True
def main():
    """main"""
    num = int(input())
    check = is_prime(num)
    if check:
        print("YES")
    else:
        print("NO")
main()

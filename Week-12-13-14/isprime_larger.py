"""isprime_larger"""
import math
def is_prime(num):
    """return prime"""
    if num < 2:
        return False
    if num == 2:
        return True
    if not num % 2:
        return False
    sqrt_num = int(math.sqrt(num)) + 1
    for i in range(3, sqrt_num, 2):
        if not num % i:
            return False
    return True

def main():
    """main"""
    num = int(input())
    result = "True" if is_prime(num) else "False"
    print(result)
main()

"""GCD_N"""
import math
def main(n):
    """main"""
    num_lst = []
    for _ in range(n):
        num = int(input())
        num_lst.append(num)
    print(math.gcd(*num_lst))
main(int(input()))

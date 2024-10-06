"""GCD_v2"""
def main(num1, num2):
    """main"""
    while num2:
        num1, num2 = num2, num1 % num2
    print(num1)
main(int(input()), int(input()))

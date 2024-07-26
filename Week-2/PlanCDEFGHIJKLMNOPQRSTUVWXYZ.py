""""PlanCDEFGHIJKLMNOPQRSTUVWXYZ"""
def main():
    """main"""
    order = input()
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    if order == "Ascend":
        if num1 > num2:
            num1, num2 = num2, num1
        if num2 > num3:
            num2, num3 = num3, num2
        if num1 > num2:
            num1, num2 = num2, num1
    elif order == "Descend":
        if num1 < num2:
            num1, num2 = num2, num1
        if num2 < num3:
            num2, num3 = num3, num2
        if num1 < num2:
            num1, num2 = num2, num1
    print(f"{num1:.2f}, {num2:.2f}, {num3:.2f}")
main()

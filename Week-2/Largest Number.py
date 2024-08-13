"""Largest Number"""
def main(num1, num2, num3):
    """main"""
    num1, num2, num3 = str(num1), str(num2), str(num3)
    if num1 + num2 > num2 + num1:
        if num1 + num3 > num3 + num1:
            if num2 + num3 > num3 + num2:
                result = num1 + num2 + num3
            else:
                result = num1 + num3 + num2
        else:
            result = num3 + num1 + num2
    else:
        if num2 + num3 > num3 + num2:
            if num1 + num3 > num3 + num1:
                result = num2 + num1 + num3
            else:
                result = num2 + num3 + num1
        else:
            result = num3 + num2 + num1
    return int(result)
a = int(input())
b = int(input())
c = int(input())
print(main(a, b, c))

"""Water"""
n = int(input())
a = float(input())
b = float(input())
c = float(input())
d = float(input())

def calculate(use, price, value, price2, money):
    """calculate"""
    if use <= value:
        bill = use * price
    else:
        bill = value * price + (use - value) * price2
    return 0 if bill <= money else bill

def main():
    """main"""
    total = 0
    for _ in range(n):
        use = float(input())
        total += calculate(use, a, b, c, d)
    print(f"{total:.2f}")
main()

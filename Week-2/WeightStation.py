"""WeightStation"""
def main():
    """Calculation of rod bun took"""
    avg = float(input())
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    num4 = 4 * avg - (num1 + num2 + num3)
    ovr =  num1 + num2 + num3 + num4
    if ovr > 15000:
        print("Overweight")
        return
    unbalance = avg / 2
    if (abs(num1 - avg) > unbalance or
        abs(num2 - avg) > unbalance or
        abs(num3 - avg) > unbalance or
        abs(num4 - avg) > unbalance):
        print("Unbalance")
        return
    print(f"Pass {num4:.2f}")
main()

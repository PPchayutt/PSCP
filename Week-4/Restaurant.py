"""Restaurant"""
def main(a, b, c, d):
    """main"""
    if a == b:
        print("Yes")
    elif a < b:
        total = a + d
        discount = total * (c / 100)
        price_after_dis = total - discount
        different = price_after_dis - a
        different = abs(different)
        if price_after_dis > a:
            print(f"No {different:.3f}")
        elif price_after_dis < a:
            print(f"Yes {different:.3f}")
        else:
            print("Yes")
main(float(input()), float(input()), float(input()), float(input()))

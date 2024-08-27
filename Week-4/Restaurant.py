"""Restaurant"""
def main(a, b, c, d):
    """main"""
    if a >= b:
        total = a + d
        discount1 = a * (c / 100)
        discount2 = total * (c / 100)
        price_after_dis1 = a - discount1
        price_after_dis2 = total - discount2
        different1 = price_after_dis1 - a
        different2 = price_after_dis2 - a
        if abs(different1) > abs(different2):
            print(f"No {abs(different1 - different2):.3f}")
        else:
            print("Yes")
    elif a < b:
        total = a + d
        discount = total * (c / 100)
        price_after_dis = total - discount
        different = price_after_dis - a
        if price_after_dis > a:
            print(f"No {abs(different):.3f}")
        elif price_after_dis < a:
            print(f"Yes {abs(different):.3f}")
        else:
            print("Yes")
main(float(input()), float(input()), float(input()), float(input()))

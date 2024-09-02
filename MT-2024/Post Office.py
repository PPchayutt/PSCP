"""Post Office"""
def mailing(n, m):
    """calculate price"""
    envelop_price = 0
    package_price = 0
    for _ in range(n):
        envelop_weight = float(input())
        if envelop_weight <= 10:
            envelop_price += 16
        elif envelop_weight <= 20:
            envelop_price += 18
        elif envelop_weight <= 100:
            envelop_price += 23
        elif envelop_weight <= 250:
            envelop_price += 28
        elif envelop_weight <= 500:
            envelop_price += 33
        elif envelop_weight <= 1000:
            envelop_price += 48
        else:
            envelop_price += 68
    for _ in range(m):
        package_weight = float(input())
        if package_weight <= 500:
            package_price += 45
        elif package_weight <= 1000:
            package_price += 55
        else:
            package_price += 70
    total = (envelop_price + (13 * n)) + (package_price + (15 * m))
    print(total)
mailing(int(input()), int(input()))

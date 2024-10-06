"""Tax"""
def calculate_tax(age, cc):
    """calculate"""
    if cc <= 600:
        tax = cc * 0.5
    elif cc <= 1800:
        tax = 600 * 0.5 + (cc - 600) * 1.5
    else:
        tax = 600 * 0.5 + 1200 * 1.5 + (cc - 1800) * 4
    if age >= 10:
        discount = 0.5
    elif age >= 9:
        discount = 0.4
    elif age >= 8:
        discount = 0.3
    elif age >= 7:
        discount = 0.2
    elif age >= 6:
        discount = 0.1
    else:
        discount = 0
    final_tax = tax * (1 - discount)
    return round(final_tax, 2)

def main(age, cc):
    """main"""
    result = calculate_tax(age, cc)
    print(f"{result:.2f}")
main(int(input()), int(input()))

"""RuleofThree"""
def main(count):
    """main"""
    best_value = None
    best_price = None
    best_size = None
    for _ in range(count):
        price = float(input())
        size = float(input())
        value = size / price
        if best_value is None or value > best_value or (value == best_value and price < best_price):
            best_value = value
            best_price = price
            best_size = size
    print(f"{best_price:.2f} {best_size:.2f}")
main(int(input()))

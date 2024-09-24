"""Stamps"""
def calculate_bill(n, a, b, c, d):
    """calculate the money"""
    total_paid = 0
    stamps = 0
    for _ in range(n):
        bill = int(input())
        if c and d :
            discount = min(bill, (stamps // c) * d)
            stamps_used = (discount + d - 1) // d * c
            stamps -= stamps_used
        else:
            discount = 0
        actual_bill = max(0, bill - discount)
        total_paid += actual_bill
        if a:
            new_stamps = (actual_bill // a) * b
            stamps += new_stamps
    print(total_paid)
    print(stamps)
calculate_bill(int(input()), int(input()), int(input()), int(input()), int(input()))

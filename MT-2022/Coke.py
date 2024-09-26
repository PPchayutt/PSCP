"""Coke"""
def total(oldprice, exchange, newprice, want):
    """total"""
    price = oldprice * want
    if not exchange:
        print(price)
    else:
        discount = int((want - 1) / exchange)
        price = (discount * newprice) + ((want - discount) * oldprice)
        print(price)
total(int(input()), int(input()), int(input()), int(input()))

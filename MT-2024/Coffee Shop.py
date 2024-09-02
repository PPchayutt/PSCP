"""Coffee Shop"""
def promotion(price, percent1, percent2, pro_price, cup):
    """calculate price"""
    pro1 = price + (cup - 1) * price * (1 - percent1 / 100)
    pro2 = price * cup
    if pro2 >= pro_price:
        pro2 = pro2 * (1- percent2 / 100)
    if pro2 <= pro1:
        print(2)
        print(f"{pro2:.2f}")
    else:
        print(1)
        print(f"{pro1:.2f}")
promotion(float(input()), float(input()), float(input()), float(input()), int(input()))

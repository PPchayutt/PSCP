"""IT Business"""
def business(account, wallet):
    """money"""
    error_count = 0
    while True:
        if error_count >= 3:
            print(f"{account:.2f}")
            print(f"{wallet:.2f}")
            break
        transaction = input()
        if transaction == "end":
            print(f"{account:.2f}")
            print(f"{wallet:.2f}")
            break
        if transaction[0] == "W":
            amount = float(transaction[2:])
            if amount > account:
                error_count += 1
                continue
            if amount <= account:
                account -= amount
                wallet += amount
                error_count = 0
                continue
        if transaction[0] == "D":
            amount = float(transaction[2:])
            if amount > wallet:
                error_count += 1
                continue
            if amount <= wallet:
                wallet -= amount
                account += amount
                error_count = 0
                continue
business(float(input()), float(input()))

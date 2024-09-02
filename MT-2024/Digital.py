"""Digital"""
def digital(name, isthai, havehome, age, income, deposit):
    """digital wallet"""
    if isthai in ("Yes", "True") and havehome in ("Yes", "True") \
and age >= 16 and income <= 840000 and deposit <= 500000:
        print(f"Congratulations! {name} is qualified to receive a digital wallet \
amount of 10,000 baht, sponsored by all taxpayers in Thailand.")
    else:
        print(f"Unfortunately, {name} is not qualified.")
digital(input(), input(), input(), float(input()), float(input()), float(input()))

"""Milk"""
def main(price, need, cap, money):
    """main"""
    bottles = money // price
    caps = bottles
    while caps >= need > 0:
        new_bottles = (caps // need) * cap
        bottles += new_bottles
        caps = (caps % need) + new_bottles
    print(bottles)
main(int(input()), int(input()), int(input()), int(input()))

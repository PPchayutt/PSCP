"""Donut""" 
def main(a, b, c, d):
    """main"""
    donut_per_sets = b + c
    sets_need = d // donut_per_sets
    total_coast = sets_need * (a * b)
    total_donuts = sets_need * donut_per_sets
    remain_of_money = d - total_donuts
    if remain_of_money >= b:
        total_donuts += donut_per_sets
        total_coast += a * b
    else:
        total_donuts += remain_of_money
        total_coast += remain_of_money * a
    print(total_coast, total_donuts)
main(int(input()), int(input()), int(input()), int(input()))

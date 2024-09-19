"""Lotto"""
def main():
    """main"""
    prize_1 = input()
    prize_2 = input()
    prize_3_first_1 = input()
    prize_3_first_2 = input()
    prize_3_end_1 = input()
    prize_3_end_2 = input()
    my_lotto = input()
    my_prize = 0
    prize_1_up, prize_1_down = int(prize_1) + 1, int(prize_1) - 1
    prize_1_up -= 1000000 if prize_1_up > 999999 else 0
    prize_1_down += 1000000 if prize_1_down < 0 else 0
    prize_1_up, prize_1_down = f"{prize_1_up:>06}", f"{prize_1_down:>06}"
    if my_lotto == prize_1:
        my_prize += 6000000
    if my_lotto == prize_1_up:
        my_prize += 100000
    if my_lotto == prize_1_down:
        my_prize += 100000
    if my_lotto[-2:] == prize_2:
        my_prize += 2000
    if my_lotto[:3] == prize_3_first_1:
        my_prize += 4000
    if my_lotto[:3] == prize_3_first_2:
        my_prize += 4000
    if my_lotto[-3:] == prize_3_end_1:
        my_prize += 4000
    if my_lotto[-3:] == prize_3_end_2:
        my_prize += 4000
    print(my_prize)
main()

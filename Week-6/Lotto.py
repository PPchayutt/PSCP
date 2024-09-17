"""Lotto"""
def main():
    """main"""
    first_prize = input()
    last_2_digits = input()
    front_3_digits_1 = input()
    front_3_digits_2 = input()
    last_3_digits_1 = input()
    last_3_digits_2 = input()
    ticket_number = input()
    total_prize = 0
    if ticket_number == first_prize:
        total_prize += 6000000
    if ticket_number[-2:] == last_2_digits:
        total_prize += 2000
    if ticket_number[:3] in [front_3_digits_1, front_3_digits_2]:
        total_prize += 4000
    if ticket_number[-3:] in [last_3_digits_1, last_3_digits_2]:
        total_prize += 4000
    if first_prize == "000000":
        nearby_prizes = ["000001", "999999"]
    elif first_prize == "999999":
        nearby_prizes = ["999998", "000000"]
    elif first_prize == "000001":
        nearby_prizes = ["000000", "000002"]
    elif first_prize == "999998":
        nearby_prizes = ["999997", "999999"]
    else:
        nearby_prizes = [f"{int(first_prize)-1:06d}", f"{int(first_prize)+1:06d}"]
    if ticket_number in nearby_prizes:
        total_prize += 100000
    print(total_prize)
main()

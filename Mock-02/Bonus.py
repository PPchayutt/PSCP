"""Bonus"""
def main(salary, year, month):
    """main Bonus"""
    if month >= 10:
        year += 1
    bonus = min(year, 20) * salary
    bonus = min(bonus, 1000000)
    bonus = max(bonus, 5000)
    print(bonus)
main(int(input()), int(input()), int(input()))

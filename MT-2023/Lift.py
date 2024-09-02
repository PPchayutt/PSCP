"""Lift"""
def main(people, lw):
    """main"""
    total = 0
    has_adult = False
    for _ in range(people):
        age = int(input().strip())
        weight = float(input().strip())
        total += weight
        if age >= 12:
            has_adult = True
    if total > lw or people > 0 and not has_adult:
        print("Not Safe")
    else:
        print("Safe")
main(int(input().strip()), float(input().strip()))

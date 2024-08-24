"""Lift"""
def main(people, lw):
    """main"""
    total = 0
    safe_or_not = False
    for _ in range(people):
        age = int(input().strip())
        weight = float(input().strip())
        total += weight
        if age >= 12:
            safe_or_not = True
    if total >= lw or not safe_or_not:
        print("Not Safe")
    else:
        print("Safe")
main(int(input().strip()),float(input().strip()))

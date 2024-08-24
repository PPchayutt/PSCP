"""Lift"""
def main(people, lw,):
    """main"""
    total = 0
    safe_or_not = '_'
    for _ in range(people):
        age = int(input())
        weight = float(input())
        total += weight
        if age >= 12:
            safe_or_not += 'Safe'
        else:
            safe_or_not += 'No'
    search = safe_or_not.find('Safe')
    if total >= lw or search == -1:
        print("Not Safe")
    else:
        print("Safe")
main(int(input()),float(input()))

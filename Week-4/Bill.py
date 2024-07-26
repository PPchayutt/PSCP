"""Bill"""
cost = float(input())
CHARGE = cost * 0.1
if CHARGE < 50:
    CHARGE = 50
elif CHARGE > 1000:
    CHARGE = 1000

total = (cost + CHARGE) + ((cost + CHARGE) * 0.07)
print(f"{total:.2f}")

"""BTSMRT"""
def bts(day,age,height):
    """mrt"""
    if day == "Children Day":
        if age < 14 and height <= 140:
            print("FREE")
        elif age < 14 and height < 90:
            print("FREE")
        else:
            print("PAY")
    elif day == "Senior Day":
        if age < 14 and height < 90:
            print("FREE")
        elif age >= 60:
            print("FREE")
        else:
            print("PAY")
    elif day == "Normal Day":
        if age < 14 and height < 90:
            print("FREE")
        else:
            print("PAY")
bts(input(),float(input()),float(input()))

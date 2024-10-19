"""Alcolhol"""
def main(sex, weight, driving, cc, alc):
    """main"""
    can = int(input())
    rest = int(input())
    drank = alc*cc/100*can
    limit = 0
    if sex == "Male":
        limit = drank / (weight*0.68*10)
    elif sex == "Female":
        limit = drank / (weight*0.55*10)
    minus = 0.015 * rest
    bruh = limit-minus
    if bruh <= 0.05 and driving == "Yes":
        print("Safe")
    else:
        print("Not Safe")
main(input(),float(input()),input(),float(input()),float(input()))

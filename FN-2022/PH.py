"""PH"""
def main(num):
    """main"""
    if 0 <= num < 7:
        print("acidic")
    elif num == 7:
        print("neutral")
    elif 7 < num <= 14:
        print("akaline")
    else:
        print("error")
main(float(input()))

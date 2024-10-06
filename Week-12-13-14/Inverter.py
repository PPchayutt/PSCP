"""Inverter"""
def main():
    """main"""
    num = input()
    num_inverse = num.translate(str.maketrans("01", "10"))
    num_inverse = int(num_inverse)
    if not num_inverse:
        print("")
    else:
        print(num_inverse)
main()

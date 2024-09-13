"""Easy Histogram"""
def main():
    """main"""
    text = input()
    dct = {}
    az = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"
    for i in text:
        if i.isalpha():
            if i in dct:
                dct[i] += 1
            else:
                dct[i] = 1
    for i in az:
        if i in dct:
            print(f"{i} = {dct[i]}")
main()

"""Parity"""
def main(text, condition):
    """main"""
    count = 0
    for i in text:
        if i == "1":
            count+=1
    if condition == "Even":
        if not count % 2:
            print(text + "0")
        else:
            print(text + "1")
    elif condition == "Odd":
        if not count % 2:
            print(text + "1")
        else:
            print(text + "0")
main(input(), input())

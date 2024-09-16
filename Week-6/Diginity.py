"""Diginity"""
def main():
    """ main """
    code = input()
    check = code
    while len(code) != 1:
        carry = 0
        for i in code:
            carry += int(i)
        code=str(carry)
    if check != "0":
        print(code)
        main()
main()

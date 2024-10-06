"""Roman"""
def main():
    """main"""
    result = 0
    number = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    roman_num = input()
    roman_num = roman_num.replace("IV","IIII")
    roman_num = roman_num.replace("IX","VIIII")
    roman_num = roman_num.replace("XL","XXXX")
    roman_num = roman_num.replace("XC","LXXXX")
    roman_num = roman_num.replace("CD","CCCC")
    roman_num = roman_num.replace("CM","DCCCC")
    for i in roman_num:
        result += number[i]
    print(result)
main()

"""PhoneNumber"""
def main(tel, teltype):
    """main"""
    if teltype == "Domestic":
        if len(tel) == 9:
            tel3 = tel[5:]
            tel2 = tel[1:5]
            print(f"0 {tel2} {tel3}")
        elif len(tel) == 10:
            tel3 = tel[6:]
            tel2 = tel[2:6]
            print(f"0{tel[1]} {tel2} {tel3}")
    elif teltype == "International":
        if len(tel) == 9:
            tel3 = tel[5:]
            tel2 = tel[1:5]
            print(f"+66 {tel2} {tel3}")
        elif len(tel) == 10:
            tel3 = tel[6:]
            tel2 = tel[2:6]
            print(f"+66{tel[1]} {tel2} {tel3}")
main(input(), input())

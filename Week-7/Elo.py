"""Elo"""
def main(ra,rb,text):
    """main"""
    if text == "A":
        EA =  1 / (1+(10**((rb-ra)/400)))
        print(f"{EA:.2f}")
    if text == "B":
        EB =  1 / (1+(10**((ra-rb)/400)))
        print(f"{EB:.2f}")
main(int(input()),int(input()),input())

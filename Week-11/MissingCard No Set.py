"""MissingCard No Set"""
def main():
    """main"""
    og_card_list = ["AS","KS","QS","JS","10S","9S","8S","7S","6S","5S","4S",\
                    "3S","2S","AH","KH","QH","JH","10H","9H","8H","7H","6H",\
                    "5H","4H","3H","2H","AD","KD","QD","JD","10D","9D","8D"\
                    ,"7D","6D","5D","4D","3D","2D","AC","KC","QC","JC","10C"\
                    ,"9C","8C","7C","6C","5C","4C","3C","2C"]
    card_list = []
    for _ in range(51):
        text = input()
        card_list.append(text)
    for i in og_card_list:
        if i not in card_list:
            print(i)
main()

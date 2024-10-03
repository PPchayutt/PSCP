"""AndAgainAndAgainAndAgainAndAgainAndAgainAndAgain"""
def main():
    """main"""
    count = 0
    check_pass = []
    vowels = ["a","e","i","o","u"]
    text = input().replace(".","")
    text = text.split()
    for i in text:
        for j in i:
            if j in vowels:
                count += 1
            if count >= 2:
                check_pass.append(i)
                count = -999
        count = 0
    count = 0
    result = sorted(check_pass)
    if result == []:
        print("Nope")
    else:
        for i in result:
            print(i)
main()

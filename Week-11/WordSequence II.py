"""WordSequence II"""
def main():
    """main"""
    text1 = input()
    text2 = input()
    len_text1 = len(text1)
    len_text2 = len(text2)
    if len_text1 > len_text2:
        for i in range(len_text1):
            print(f"{text2[:i]}{text1[i:]}")
        print(text2)
    else:
        for i in range(len_text2):
            print(f"{text2[:i]}{text1[i:]}")
        print(text2)
main()

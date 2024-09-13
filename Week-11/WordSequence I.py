"""WordSequence I"""
def main():
    """main"""
    text = input()
    len_text = len(text)
    for i in range(len_text):
        print(text[:i+1])
main()

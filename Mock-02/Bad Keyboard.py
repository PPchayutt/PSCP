"""Bad Keyboard"""
def main(text):
    """main"""
    corrected_text = text.translate(str.maketrans("ioIO", "oiOI"))
    print(corrected_text)
main(input())

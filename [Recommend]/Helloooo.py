"""Heloooo"""
def main(text):
    """main"""
    pos = len(text)-1
    vowel = ("a","e","i","o","u","A","E","I","O","U")
    texthavevowel = False
    for i in reversed(text):
        if i in vowel:
            texthavevowel = True
            break
        pos -= 1
    if texthavevowel:
        print(text[:pos] + text[pos]*4 + text[pos+1:])
    else:
        print(text)
main(str(input()))

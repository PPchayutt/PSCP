"""Stuttering"""
def main(text):
    """main"""
    words = text.split()
    corrected = [words[0]]
    for word in words[1:]:
        if word != corrected[-1]:
            corrected.append(word)
    print(' '.join(corrected))
main(input())

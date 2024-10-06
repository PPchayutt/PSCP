"""HorizontalHistogram"""
def main():
    """main"""
    dic_alpha = {}
    text = input()
    sorted_text = list(text)
    sorted_text.sort()
    sorted_text.sort(key = str.isupper)
    for i in sorted_text:
        if i in dic_alpha:
            dic_alpha[i] += 1
        else:
            dic_alpha[i] = 1
    for i,count in dic_alpha.items():
        hypen = ""
        for j in range(count):
            if j > 0 and not j % 5:
                hypen += "|"
            hypen += "-"
        print(f"{i} : {hypen}")
main()

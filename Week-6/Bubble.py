"""Bubble"""
def main():
    """main"""
    text = input() + "||||"
    i = 0
    step = 0
    while text[i] != "|":
        if text[i] == "^":
            if text[i+1] != " ":
                i += 1
                step += 1
            else:
                print("IMPOSSIBLE")
                print(text.find("|") - i)
                return
        elif text[i] == "o":
            if text[i+1] != " ":
                i += 1
                step += 1
            else:
                if text[i-1] in "O" and text[i+1:i+4] not in "   ":
                    i -= 1
                else:
                    print("IMPOSSIBLE")
                    print(text.find("|") - i)
                    return
        elif text[i] in "O" and text[i+1:i+4] not in "   ":
            for far in range(3, 0, -1):
                if text[i+far] not in " ":
                    i += far
                    step += 1
                    break
        else :
            print("IMPOSSIBLE")
            print(text.find("|") - i)
            return
    print("POSSIBLE")
    print(step)
main()

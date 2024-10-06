"""WPM"""
age = input()
wpm = int(input())

def kid():
    """kid"""
    if wpm < 11:
        return "Very Slow"
    if 11 <= wpm <= 20:
        return "Slow"
    if 21 <= wpm <= 30:
        return "Average"
    if 31 <= wpm <= 40:
        return "Fast"
    return "Very Fast"

def adult():
    """adult"""
    if wpm < 26:
        return "Very Slow"
    if 26 <= wpm <= 35:
        return "Slow/Beginner"
    if 26 <= wpm <= 45:
        return "Intermediate/Average"
    if 46 <= wpm <= 65:
        return "Fast/Advanced"
    if 66 <= wpm <= 80:
        return "Very Fast"
    return "Insane"

def main():
    """main"""
    result = ""
    if age == "Kids":
        result = kid()
    if age == "Adults":
        result = adult()
    print(result)
main()

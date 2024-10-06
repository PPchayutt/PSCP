"""LetterFrequency"""
def main(txt):
    """main"""
    result = {}
    for i in txt.lower():
        if i not in result and i.isalpha():
            result[i] = 1
        elif i in result:
            result[i] += 1
    final_result = max(result, key=result.get)
    print(final_result)
main(input())

"""B - Fully pair"""
def find_unpaired_letters(s):
    """find"""
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    unpaired = []
    for char in s:
        if char_count[char] % 2 and char not in unpaired:
            unpaired.append(char)
    if not unpaired:
        return "fully paired"
    return ''.join(unpaired)
input_string = input()
RESULT = find_unpaired_letters(input_string)
print(RESULT)

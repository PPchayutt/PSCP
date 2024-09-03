"""Run Length Encoding"""
def main():
    """main"""
    input_string = input().strip()
    if not input_string:
        print("")
        return
    encoded_string = ""
    current_char = input_string[0]
    count = 1
    for char in input_string[1:]:
        if char == current_char:
            count += 1
        else:
            encoded_string += f"{count}{current_char}"
            current_char = char
            count = 1

    encoded_string += f"{count}{current_char}"
    print(encoded_string)
main()

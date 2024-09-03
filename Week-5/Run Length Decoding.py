"""Run Length Decoding"""
def main():
    """main"""
    encoded_string = input().strip()
    decoded_string = ""
    count = 0
    for char in encoded_string:
        if char.isdigit():
            count = count * 10 + int(char)
        else:
            decoded_string += char * count
            count = 0
    print(decoded_string)
main()

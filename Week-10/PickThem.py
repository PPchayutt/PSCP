"""PickThem"""
import json
def main(json_input):
    """main"""
    lst = json.loads(json_input)
    even_number = [num for num in lst if not num % 2]
    if even_number:
        for num in even_number:
            print(num)
    else:
        print("Nope")
main(input())

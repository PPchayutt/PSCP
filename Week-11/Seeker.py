"""Seeker"""
import re
def main(text):
    """main"""
    numbers = [int(num) for num in re.findall(r'\d+', text)]
    total = sum(numbers)
    print(total)
main(input())

"""Harshad"""
def main():
    """main"""
    def is_divisible(num):
        abs_num = abs(num)
        digit_sum = sum(int(digit) for digit in str(abs_num))
        if not digit_sum:
            return False
        return not num % digit_sum
    numbers = [int(input()) for _ in range(10)]
    for num in numbers:
        if is_divisible(num):
            print("Yes")
        else:
            print("No")
main()

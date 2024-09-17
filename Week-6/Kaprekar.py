"""Kaprekar"""
def main(n):
    """main"""
    def rearrange_desc(num):
        """Rearrange digits in descending"""
        digits = list(num)
        for i, _ in enumerate(digits):
            for j in range(i + 1, len(digits)):
                if digits[i] < digits[j]:
                    digits[i], digits[j] = digits[j], digits[i]
        return ''.join(digits)
    def rearrange_asc(num):
        """Rearrange digits in ascending"""
        digits = list(num)
        for i, _ in enumerate(digits):
            for j in range(i + 1, len(digits)):
                if digits[i] > digits[j]:
                    digits[i], digits[j] = digits[j], digits[i]
        return ''.join(digits)
    count = 0
    while n != 6174:
        num_str = f"{n:04d}"
        high_str = rearrange_desc(num_str)
        low_str = rearrange_asc(num_str)
        high = int(high_str)
        low = int(low_str)
        n = high - low
        count += 1
    print(count)
main(int(input()))

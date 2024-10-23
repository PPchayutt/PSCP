"""PrasomSib"""
def main():
    """main"""
    digits = input().strip()
    n = len(digits)
    count = 0
    for i in range(n):
        total = 0
        for j in range(i, n):
            total += int(digits[j])
            if total == 10:
                count += 1
            elif total > 10:
                break
    print(count)
main()

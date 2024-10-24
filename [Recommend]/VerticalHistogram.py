"""VerticalHistogram"""
def main():
    """main"""
    text = input()
    alpa = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    result = {}
    for alpha in alpa:
        result[alpha] = 0
        for char in text:
            if char == alpha:
                result[alpha] += 1
    maximum = result[max(result, key=result.get)]
    for count in range(maximum, 0, -1):
        if count < 10:
            print(f" {count} ", end='')
        else:
            print(f"{count} ", end='')
        for alpha in alpa:
            if result[alpha] >= count and result[alpha]:
                print(" *", end='')
            elif not result[alpha]:
                continue
            else:
                print("  ", end='')
        print()
    print(" " * 3, end='')
    for alpha in alpa:
        if result[alpha]:
            print(f" {alpha}", end='')
main()

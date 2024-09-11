"""One For All"""
def main(num):
    """main"""
    count = 0
    ans = ""
    for _ in range(num):
        txt = input()
        count += 1
        if count == num:
            ans += txt + "_" + str(num)
        elif not count % 2:
            ans += txt + "-" * count
        elif count % 2:
            ans += txt + "*" * count
    print(ans)
main(int(input()))

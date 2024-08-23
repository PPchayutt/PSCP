"""Sequence XII"""
def main(num):
    """main"""
    for i in range(-num + 1, num):
        for j in range(-num + 1, num):
            value = num - abs(abs(i) - abs(j))
            print(f"{value:02}", end =" ")
        print()
main(int(input()))

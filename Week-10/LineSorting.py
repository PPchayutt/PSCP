"""LineSorting"""
def main(n):
    """main"""
    textlist = []
    for _ in range(n):
        text = input()
        textlist.append(text)
    textlist.sort(key = len)
    for i in textlist:
        print(i)
main(int(input()))

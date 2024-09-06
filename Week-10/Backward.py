"""Backward"""
def main():
    """main"""
    lst = []
    text = None
    while text != "NULL":
        text = input()
        lst.append(text)
    lst.remove("NULL")
    lst.reverse()
    for i in lst:
        print(i)
main()

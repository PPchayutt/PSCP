"""Pringles"""
def main(line1, line2, line3, line4):
    """main"""
    lenght, count, line3 = len( line1.strip()), line2.count(")"), str(line3)
    if int(line4) >= lenght:
        print(count)
        print("None.")
        print("_" * lenght)
        print(" " * lenght + "|")
        print("_" * lenght)
        return
    package, eaten = "", 0
    for i in range(lenght):
        if i < int(line4) and line2[i] == ")":
            package += " "
            eaten += 1
        else:
            package += line2[i]
    print(eaten)
    print("There are still some left." if count else "None.")
    print("_" * lenght)
    print(package + "|")
    print("_" * lenght)
main(input(), input(), input(), input())

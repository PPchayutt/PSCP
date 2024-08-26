"""Pringles"""
def main():
    """main"""
    line1 = input()
    line2 = input()
    line3 = input()
    finger_size = int(input())
    total = line2.count(")") + line2.count(" ")
    to_remove = min(finger_size, total)
    new_line2 = ""
    removed_count = 0
    for char in line2:
        if removed_count < to_remove and char == ")":
            new_line2 += " "
            removed_count += 1
        else:
            new_line2 += char
    remaining = new_line2.count(")")
    print(removed_count)
    if not remaining:
        print("None.")
    else:
        print("There are still some left.")
    print(line1)
    print(new_line2)
    print(line3)
main()

"""Bus Seat"""
def main():
    """main"""
    column = int(input())
    rows = int(input())
    number = int(input())
    count = 0
    check = column
    for i in range(1,column+1):
        if count == 2:
            count = 0
            print()
        for _ in range(rows):
            if check == number:
                print('XX',end=" ")
            else:
                print(f'{check:>02}',end=" ")
            check += column
        if i < column:
            print()
        check = column
        check -= i
        count += 1
main()

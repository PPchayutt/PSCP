"""Books"""
def main(books, pages, num_x, num_y):
    """main"""
    copy_of_pages, copy_of_books, days, bypass = pages, 0, 0, False
    for _ in range(10 ** 8):
        if copy_of_books >= books:
            break
        while copy_of_pages > 0:
            today = pages * ((num_x + days)/(num_y + days))
            if today % 1:
                today += 1 - (today % 1)
            copy_of_pages -= today
            days += 1
        copy_of_books += 1
        copy_of_pages = pages
        if today == pages:
            bypass = True
            break
    if bypass:
        days += books - copy_of_books
    print(days)
main(int(input()), int(input()), int(input()), int(input()))

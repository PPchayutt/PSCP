"""BookWorm"""
def calculate_max_books(total_time, book_times):
    """calculate time of reading a books"""
    book_times.sort()
    books_read = 0
    time_spent = 0
    for book_time in book_times:
        if time_spent + book_time <= total_time:
            time_spent += book_time
            books_read += 1
        else:
            break
    return books_read

def main():
    """main"""
    num_test_cases = int(input())
    for _ in range(num_test_cases):
        total_time = float(input())
        num_books = int(input())
        book_times = [float(input()) for _ in range(num_books)]
        max_books = calculate_max_books(total_time, book_times)
        print(max_books)
main()

"""Palindrome"""
def is_palindrome(time):
    """is_palindrome"""
    return time == time[::-1]

def next_time(hour, mn):
    """next_time"""
    mn += 1
    if mn == 60:
        hour += 1
        mn = 0
    if hour == 24:
        hour = 0
    return hour, mn

def format_time(hour, mn):
    """format_time"""
    if hour < 10:
        return f"{hour}:{mn:02d}"
    return f"{hour}:{mn:02d}"

def parse_time(time_str):
    """parse_time"""
    colon_index = time_str.index(':')
    hour = int(time_str[:colon_index])
    mn = int(time_str[colon_index+1:])
    return hour, mn

def find_next_palindromes(start_time, count):
    """find_next_palindromes"""
    hour, mn = parse_time(start_time)
    found = 0

    while found < count:
        hour, mn = next_time(hour, mn)
        time_str = format_time(hour, mn)
        if is_palindrome(time_str.replace(':', '')):
            print(time_str)
            found += 1

n = int(input())
current_time = input()

find_next_palindromes(current_time, n)

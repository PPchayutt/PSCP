"""Timing II"""
def main():
    """main"""
    second = int(input())
    if second < 864000000:
        day = second // 86400
        second -= day * 86400
        hour = second // 3600
        second -= hour * 3600
        minute = second // 60
        second -= minute * 60
        print(f"{day:04d}:{hour:02d}:{minute:02d}:{second:02d}")
    else:
        print("ERR_:__:__:__")
main()

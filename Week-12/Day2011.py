"""Day2011"""
def main():
    '''doc'''
    month = {
        0 : 0,
        1 : 31,
        2 : 28,
        3 : 31,
        4 : 30,
        5 : 31,
        6 : 30,
        7 : 31,
        8 : 31,
        9 : 30,
        10 : 31,
        11 : 30,
        12 : 31
    }
    day = {
        0 : 'Friday',
        1 : 'Saturday',
        2 : 'Sunday',
        3 : 'Monday',
        4 : 'Tuesday',
        5 : 'Wednesday',
        6 : 'Thursday',
    }
    dayneed = int(input())
    monthneed = int(input())
    totalday = dayneed
    for this in range(1,monthneed):
        totalday += month[this]
    print(day[totalday%7])
main()

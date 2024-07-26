"""SecondConverter"""
k = int(input())
s = int(input())
m = int(input())
h = int(input())

calc_minute, second = divmod(k, s)
calc_hour, minute = divmod(calc_minute, m)
if calc_hour >= h:
    calc_hour %= h
print(calc_hour, minute, second, sep = ":")

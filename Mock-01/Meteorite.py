"""Meteorite"""
def main():
    """main"""
    a = float(input())
    b = abs(int(input()))
    c = float(input())
    meteo = 1
    shoot_count = 0
    if not a:
        print(int(0))
    else:
        while a >= c:
            shoot_count += meteo
            a /= b
            meteo *= b
        print(shoot_count)
main()

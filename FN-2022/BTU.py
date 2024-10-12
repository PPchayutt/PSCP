"""BTU"""
def get_btu(area):
    """btu"""
    btu_table = [
        (100, 150, 5000), (151, 250, 6000), (251, 300, 7000),
        (301, 350, 8000), (351, 400, 9000), (401, 450, 10000),
        (451, 550, 12000), (551, 700, 14000), (701, 1000, 18000),
        (1001, 1200, 21000), (1201, 1400, 23000), (1401, 1500, 24000),
        (1501, 2000, 30000), (2001, 2500, 34000)
    ]
    for start, end, btu in btu_table:
        if start <= area <= end:
            return btu
    return 34000

def main(area, height, people, room_type, sun_exposure):
    """main"""
    btu = get_btu(area)
    if height > 8:
        btu += (height - 8) * 1000
    btu += max(0, people - 2) * 600
    if room_type.lower() == "kitchen":
        btu += 4000
    if sun_exposure.lower() == "facing the sun":
        btu = int(btu * 1.1)
    elif sun_exposure.lower() == "shaded":
        btu = int(btu * 0.9)
    print(btu)
main(int(input()), int(input()), int(input()), input(), input())

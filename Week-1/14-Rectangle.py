"""Rectangle"""
h = int(input())
w = int(input())
def rec_perimeter():
    """perimeter"""
    perimeter = h*2 + w*2
    print(perimeter)

def rec_area():
    """area"""
    area = h * w
    print(area)
rec_area()
rec_perimeter()

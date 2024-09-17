"""FourDirections"""
def main(text):
    """main"""
    arrows = {
        "U": ["  *  ", " *** ", "* * *", "  *  ", "  *  "],
        "D": ["  *  ", "  *  ", "* * *", " *** ", "  *  "],
        "L": ["  *  ", " *   ", "*****", " *   ", "  *  "],
        "R": ["  *  ", "   * ", "*****", "   * ", "  *  "]
    }
    for i in range(5):
        for direction in text:
            print(arrows[direction][i], end=" ")
        print()
main(input())

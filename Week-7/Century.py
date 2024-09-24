"""Century"""
def calculate_century(year_input):
    """calculate century"""
    try:
        era, year = year_input.split()
        year = int(year)
        if era == "B.E.":
            year -= 543
        elif era != "A.D.":
            return "ERROR"
        if year <= 0:
            return "ERROR"
        century = (year - 1) // 100 + 1
        return str(century)
    except ValueError:
        return "ERROR"

def main(n):
    """main"""
    years = [input() for _ in range(n)]
    for year_input in years:
        result = calculate_century(year_input)
        print(result)
main(int(input()))

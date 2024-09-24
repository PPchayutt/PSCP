"""US Interstate Number System"""
def analyze_highway(number):
    """Analyze the interstate highway number."""
    if 1 <= number <= 99:
        if number % 5 == 0:
            if number % 10 == 0:
                return "Horizontal Major Interstate", f"I-{number}"
            else:
                return "Vertical Major Interstate", f"I-{number}"
        else:
            return "Horizontal Major Interstate", f"I-{number}"
    elif 100 <= number <= 999:
        main_route = number % 100
        if main_route == 0:
            main_route = 100
        if number // 100 % 2 == 0:
            return "Even Minor Interstate", f"I-{main_route}"
        else:
            return "Odd Minor Interstate", f"I-{main_route}"
    else:
        return "Others", None
highway_number = int(input())
highway_type, main_route = analyze_highway(highway_number)
if highway_type != "Others":
    print(highway_type)
    print(main_route)
else:
    print(highway_type)

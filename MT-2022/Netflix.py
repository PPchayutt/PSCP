"""Netflix"""
def recommend_netflix_plan():
    """recommend_netflix_plan"""
    screens = int(input())
    downloads = int(input())
    unlimited = input()
    mobile_tablet = input()
    laptop_tv = input()
    hd = input()
    ultra_hd = input()

    def mobile(): return (1, 1, True, True, False, False, False, 99)
    def basic(): return (1, 1, True, True, True, False, False, 279)
    def standard(): return (2, 2, True, True, True, True, False, 349)
    def premium(): return (4, 4, True, True, True, True, True, 419)

    def meets_requirements(plan):
        """meets_requirements"""
        return (screens <= plan[0] and downloads <= plan[1] and
                (unlimited == "No" or plan[2]) and
                (mobile_tablet == "No" or plan[3]) and
                (laptop_tv == "No" or plan[4]) and
                (hd == "No" or plan[5]) and
                (ultra_hd == "No" or plan[6]))

    recommended_plans = ""
    total_cost = 0
    remaining_screens = screens

    if meets_requirements(premium()):
        premium_count = (remaining_screens - 1) // 4 + 1
        recommended_plans += f"Premium x {premium_count}\n"
        total_cost += premium_count * premium()[7]
        remaining_screens -= premium_count * 4

    if remaining_screens > 0 and meets_requirements(standard()):
        standard_count = (remaining_screens - 1) // 2 + 1
        recommended_plans += f"Standard x {standard_count}\n"
        total_cost += standard_count * standard()[7]
        remaining_screens -= standard_count * 2

    if remaining_screens > 0 and meets_requirements(basic()):
        basic_count = remaining_screens
        recommended_plans += f"Basic x {basic_count}\n"
        total_cost += basic_count * basic()[7]

    if not recommended_plans and meets_requirements(mobile()):
        mobile_count = screens
        recommended_plans += f"Mobile x {mobile_count}\n"
        total_cost += mobile_count * mobile()[7]

    if recommended_plans:
        print(recommended_plans, end="")
        print(f"Total = {total_cost} THB")
    else:
        print("No suitable plan found.")

recommend_netflix_plan()

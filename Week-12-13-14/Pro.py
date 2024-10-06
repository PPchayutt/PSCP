'''Pro'''
def pro(pro_people, pro_pay, price_per_person, come):
    '''Pro'''
    pay = 0
    promotion = come // pro_people
    not_pro = come - promotion * pro_people
    if promotion:
        pay += pro_pay * price_per_person * promotion
    if not_pro:
        pay += price_per_person * not_pro
    print(pay)
pro(int(input()), int(input()), int(input()), int(input()))

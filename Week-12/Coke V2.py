'''Coke V2'''
def coke():
    '''doc'''
    cost = int(input())
    require = int(input())
    discounted = int(input())
    need = int(input())
    if not require:
        print(cost*need)
        return
    if not need:
        print(0)
        return
    bundle = need//require
    paid = bundle*((cost*(require-1))+discounted)
    got = bundle*require
    if got < need:
        paid += cost
        got += 1
        paid += (need-got)*cost
        got += need-got
    elif got+1 > need:
        paid = paid - discounted + cost
    print(paid)
coke()

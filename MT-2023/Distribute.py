"""Distribute"""
def main(money, child):
    """main"""
    answer = 0
    if money < child or (child == 1 and money == 4):
        answer = -1
    else:
        money -= child
        quota = money // 7
        left = money % 7
        answer = quota
        if quota >= child and left:
            answer -= 1
        elif quota > child:
            answer -= 1
        elif left == 3 and (quota >= child or child - quota == 1):
            answer -= 1
        if quota > child:
            answer -= (quota - child)
        answer = max(answer, 0)
    print(answer)
main(int(input()),int(input()))

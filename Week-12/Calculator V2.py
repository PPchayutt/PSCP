'''Calculator V2'''
def calcount():
    '''count time click button on calc'''
    amount = int(input())
    count = 0
    for i in range(1,amount+1):
        count += len(str(i)) + 1
    if amount == 1:
        count -= 1
    print(count)
calcount()

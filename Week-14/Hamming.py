'''Hamming'''
def ham(txt1, txt2):
    '''ham'''
    count = 0
    lst_txt1 = list(i for i in txt1)
    lst_txt2 = list(i for i in txt2)
    length = len(lst_txt1)
    for i in range(length):
        if lst_txt1[i] != lst_txt2[i]:
            count += 1
    print(count)
ham(input(), input())

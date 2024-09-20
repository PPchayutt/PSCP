'''Scientific Notation'''
def findfirstnum(string):
    '''return first numeric found in string'''
    indexfound = -1
    for i in range(1,10):
        finding = string.find(str(i))
        if finding != -1 and (finding < indexfound or indexfound == -1):
            indexfound = finding
    return indexfound
def findlastnum(string):
    '''return last numeric found in string'''
    indexfound = -1
    for i in range(1,10):
        finding = string.rfind(str(i))
        if finding != -1 and (finding > indexfound or indexfound == -1):
            indexfound = finding
    return indexfound
def main():
    '''doc'''
    num_in = input().strip().replace(' ','')
    findexpo = num_in.find('^')
    answer = ''
    if findexpo != -1:
        power = int(num_in[findexpo+1:])
        findx = num_in.find('x')
        base = float(num_in[:findx].strip())
        answer = base*(10**power)
        if answer == int(answer):
            answer = int(answer)
    else:
        if not float(num_in):
            print(0)
            return
        negative = num_in[0] == '-'
        if num_in[0] == '.' or (negative and num_in[1] == '.'):
            num_in = '0' + num_in
        firstnum_index = findfirstnum(num_in)
        decimalpointer = num_in.find('.')
        numberneed = num_in[firstnum_index:].replace('.','')
        negative = num_in[0] == '-'
        power = 0
        if decimalpointer != -1:
            if decimalpointer < firstnum_index:
                power = -(firstnum_index-decimalpointer)
            elif decimalpointer > firstnum_index:
                power = (decimalpointer - 1) - firstnum_index
        else:
            power = len(num_in.replace('-',''))-1
        if decimalpointer in (-1,len(num_in)-1):
            numberneed = numberneed[:findlastnum(numberneed)+1]
        if len(numberneed) > 1:
            numberneed = numberneed[0] + '.' + numberneed[1:]
        if negative:
            numberneed = '-'+numberneed
        answer = f'{numberneed} x 10^{power}'
    print(answer)
main()

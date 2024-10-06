"""PrasomSib"""
def counttoten(number_string):
    """prasom"""
    count = 0
    n = len(number_string)
    for i in range(n):
        if i < n - 1:
            if int(number_string[i]) + int(number_string[i+1]) == 10:
                count += 1
            if int(number_string[i:i+2]) == 10:
                count += 1
        if i < n - 2:
            if sum(map(int, number_string[i:i+3])) == 10:
                count += 1
    print(count)
counttoten(input().strip())

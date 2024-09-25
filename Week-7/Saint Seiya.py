"""Saint Seiya"""
def seiya(second, punch):
    """seiya"""
    punchh = 0
    for i in range(2, second + 1, 2):
        if punchh < punch:
            if not i % 6:
                punchh += 1
            elif not i % 2:
                punchh += 165
        else:
            punchh += (second + 1 - i) * 12
            break
    print(punchh)
seiya(int(input()), int(input()))

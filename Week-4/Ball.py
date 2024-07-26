"""Ball"""
height = float(input())
COUNT = 0
while height >= 0.01:
    height *= 0.60
    COUNT += 1
print(COUNT-1)

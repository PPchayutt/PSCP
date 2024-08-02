"""Key"""
num = input()
KEY = 0
for i in num:
    i = int(i)
    KEY += i
lastthree = int(num[10:]) * 10
REALKEY = KEY + lastthree
if len(str(REALKEY)) > 4:
    REALKEY = str(REALKEY)
    print(REALKEY[1:])
elif len(str(REALKEY)) < 4:
    REALKEY += 1000
    print(str(REALKEY))
else:
    print(str(REALKEY))

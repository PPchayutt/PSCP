"""ChristmasTree"""
leaf = int(input())
tree = int(input())

NUM = 1
STRING = ""

for i in range(leaf):
    for j in range(1, leaf - i):
        j = j * 1
        STRING += " "
    for _ in range(i + NUM):
        _ = _ * 1
        STRING += "*"
    print(STRING)
    length = len(STRING)
    STRING = ""
    NUM += 1
for i in range(tree):
    print(("-" * 3).center(length))

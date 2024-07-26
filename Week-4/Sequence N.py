"""Sequence N"""
n = int(input())
for i in range(n):
    print("*", end="")
    for j in range(1,n-1):
        if i == j:
            print("*", end="")
        else:
            print(" ", end="")
    print("*", end="")
    print()

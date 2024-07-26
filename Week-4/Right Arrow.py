"""Right Arrow"""
k = int(input())
n = int(input())
for i in range(n // 2 + 1):
    print(" " * abs(i) + "*" * k)
for i in range(n // 2):
    print(" " * abs(n // 2 - i - 1) +  "*" * k)

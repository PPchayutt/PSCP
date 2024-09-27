"""Dart"""
import math
def calculatescore(x, y):
    """Dart"""
    distance = math.sqrt(x**2 + y**2)
    if distance <= 2:
        return 5
    if distance <= 4:
        return 4
    if distance <= 6:
        return 3
    if distance <= 8:
        return 2
    if distance <= 10:
        return 1
    return 0
def ans(n):
    """ans"""
    total_score = 0
    for _ in range(n):
        x, y = map(int, input().split())
        total_score += calculatescore(x, y)
    print(total_score)
ans(int(input()))

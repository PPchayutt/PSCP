"""Dota"""
from math import comb
def calculate(n):
    """lol"""
    if n < 1 or n > 10:
        return 0
    count = 0
    for team1 in range((n + 1) // 2, min(5, n) + 1):
        team2 = n - team1
        if abs(team1 - team2) <= 1:
            count += comb(n, team1)
    return count
n = int(input())
result = calculate(n)
print(result)

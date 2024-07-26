"""Boomerang"""
import math
x_value = int(input())
y_value = int(input())
z_value = int(input())
def f1(x):
    """1"""
    return x + 1
def f2(y):
    """2"""
    return (7*(y**3)) + (2*(y**2)) - (31*y) + 1
def f3(z):
    """3"""
    return -z
def f4(x, y):
    """4"""
    return (x + y) * (x - y)
def f5(x, y , z):
    """5"""
    return (y - math.sqrt(y**2 - 4*x*z)) / (2*x)
print(f1(x_value))
print(f2(y_value))
print(f3(z_value))
print(f4(x_value, y_value))
print(f5(x_value, y_value , z_value))

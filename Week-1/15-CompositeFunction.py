"""CompositeFunction"""
def f(x):
    """f"""
    return 2 * x

def g(x):
    """g"""
    return x / 2 + 1
x_val = float(input())
result1 = f(g(x_val))
result2 = g(f(x_val))
print(f"{result1:.2f}")
print(f"{result2:.2f}")

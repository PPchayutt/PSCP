"""Jumping"""
def print_output(num, count=3):
    """print_output"""
    if count > 0:
        print(f"Output{num}")
        print_output(num, count - 1)

def jumping(num=1):
    """jumping"""
    if num <= 4:
        print_output(num)
        jumping(num + 1)
jumping()

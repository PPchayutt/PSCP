"""Calculator"""
def main(num):
    """main"""
    if num == 1:
        return "1"
    result = "+".join(str(i) for i in range(1, num + 1)) + "+"
    return result
OUTPUT = main(int(input()))
print(len(OUTPUT))

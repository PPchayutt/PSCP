"""Easy Histogram No Dict"""
def main():
    """main"""
    text = input()
    az = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"
    for i in az:
        if i in text:
            print(f"{i} = {text.count(i)}")
main()

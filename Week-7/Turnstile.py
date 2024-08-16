"""Turnstile"""
def main():
    """main"""
    count = 0
    status = False
    text = ""
    while text != "END":
        text = input()
        if text == "C":
            status = True
        elif text == "P":
            if status is True:
                count += 1
                status = False
    print(count)
main()

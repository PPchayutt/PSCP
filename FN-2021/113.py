"""113"""
def main(text):
    """main"""
    removed = text.replace("113", "")
    while "113" in removed:
        removed = removed.replace("113", "")
    print(removed)
main(str(input()))

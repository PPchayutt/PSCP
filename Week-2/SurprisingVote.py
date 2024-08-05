"""SurprisingVote"""
def main(total, highest):
    """main"""
    second = min(total-highest, highest)
    lowest = total - highest - second
    if highest - lowest > 2:
        print("Surprising")
    else:
        print("Not surprising")
main(float(input()), float(input()))

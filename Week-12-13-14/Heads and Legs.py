"""Heads and Legs"""
def main():
    """main"""
    num = int(input())
    leg = int(input())
    rabbit, nohave = divmod(leg-2 * num, 2)
    bird = num - rabbit
    if rabbit >= 0 and bird >= 0 and not nohave:
        print(rabbit, bird)
    else:
        print("Impossible")
main()

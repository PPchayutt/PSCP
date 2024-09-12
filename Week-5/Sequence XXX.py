"""SequenceXXX"""
def main(size, num):
    """main"""
    for i in range(size):
        if not i  or i == size-1:
            for _ in range(num):
                print("*"*size, end=" ")
            print()
        else:
            for _ in range(num):
                for j in range(size):
                    if i == j or not j or j == size-1 or j == size-1-i:
                        print("*", end="")
                    else:
                        print(" ", end="")
                print("", end=" ")
            print()
main(int(input()), int(input()))

"""Sequence III"""
def main():
    """main"""
    x = int(input())
    for i in range(x):
        for j in range(1,x+1):
            print(j+(i+1), end=" ")
        print()
main()

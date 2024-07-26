"""Sequence VII"""
def main():
    """main"""
    x = int(input())
    for i in range(1,x+1):
        print(" ".join(str(j) for j in range(1, i+1)))
    for i in range(x-1,0,-1):
        print(" ".join(str(j) for j in range(1, i+1)))
main()

"""BootSequence"""
def main(x):
    """main"""
    ans = "1"
    for i in range(2,x+1):
        ans = ans + "_" + str(i)
    print(ans)
main(int(input()))

"""LastStand"""
import json
def main():
    """main"""
    num = json.loads(input())
    for i in num:
        print(str(i)[-1])
main()

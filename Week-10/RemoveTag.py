"""RemoveTag"""
import re
def main(txt):
    """main"""
    ans = re.sub(r'<.*?>'," ", txt)
    final = ans.split()
    print(final)
main(input())

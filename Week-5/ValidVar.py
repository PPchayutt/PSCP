"""ValidVar"""
def main():
    """main"""
    count = int(input())
    reserved_words = ('False', 'None', 'True', 'and',
        'as', 'assert', 'async', 'await', 'break', 'class',
        'continue', 'def', 'del', 'elif', 'else', 'except',
        'finally', 'for', 'from', 'global', 'if', 'import',
        'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass',
        'raise', 'return', 'try', 'while', 'with', 'yield' )
    punctuation = '''!"#$%&'()*+,-./:;<=>?@[\\]^`{|}~'''
    for _ in range(count):
        name = input()
        if name in reserved_words :
            print("Invalid")
        elif any(char in punctuation for char in name):
            print("Invalid")
        else:
            if name[0].isalpha() or name[0] == "_" or name[0] == " ":
                if all(c.isalnum() or c == "_" for c in name[1:len(name)]):
                    print("Valid")
                else:
                    print("Invalid")
            else:
                print("Invalid")
main()

"""Shorten"""
def main():
    """main"""
    sequence = ""
    start = None
    end = None
    first = True
    while True:
        n = int(input())
        if n == -1:
            break
        if start is None:
            start = n
            end = n
        elif n == end + 1:
            end = n
        else:
            if not first:
                sequence += ", "
            if start == end:
                sequence += f"{start}"
            else:
                sequence += f"{start}-{end}"
            start = n
            end = n
            first = False
    if start is not None:
        if not first:
            sequence += ", "
        if start == end:
            sequence += f"{start}"
        else:
            sequence += f"{start}-{end}"
    print(sequence)
main()

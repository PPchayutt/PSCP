"""Align"""
size = int(input())
align = input()
text = input()
textsize = len(text)
if align == "left":
    print(text.ljust(size))
if align == "center":
    if not (size - textsize) % 2:
        print(text.center(size))
    else:
        print(text.center(size+1))
if align == "right":
    print(text.rjust(size))

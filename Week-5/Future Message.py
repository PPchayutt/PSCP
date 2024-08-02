"""Future Message"""
text = input()
if text.isnumeric() is True:
    print("Number")
elif text.isupper() is True:
    print("Uppercase")
elif text.islower() is True:
    print("Lowercase")
elif text.istitle() is True:
    print("Title")
elif text.isspace() is True:
    print("Space")
else:
    print("Other")

'''Fever'''
def fever(temp):
    '''Fever'''
    if 36 <= temp < 38:
        print("No Fever")
    elif 38 <= temp < 39:
        print("Mild Fever")
    elif 39 <= temp < 40:
        print("High Fever")
    else:
        print("Very High Fever")
fever(float(input()))

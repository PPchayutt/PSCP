"""iPhone 13 Again"""
def iphone13mini(model, storage):
    """ip13mini"""
    if model == "iPhone 13 mini":
        if storage == "128 GB":
            print(25900)
        elif storage == "256 GB":
            print(29900)
        elif storage == "512 GB":
            print(37900)
        else:
            print("Not Available")

def iphone13(model, storage):
    """ip13"""
    if model == "iPhone 13":
        if storage == "128 GB":
            print(29900)
        elif storage == "256 GB":
            print(33900)
        elif storage == "512 GB":
            print(41900)
        else:
            print("Not Available")

def iphone13pro(model, storage):
    """ip13p"""
    if model == "iPhone 13 Pro":
        if storage == "128 GB":
            print(38900)
        elif storage == "256 GB":
            print(42900)
        elif storage == "512 GB":
            print(50900)
        elif storage == "1 TB":
            print(58900)
        else:
            print("Not Available")

def iphone13promax(model, storage):
    """ip13pm"""
    if model == "iPhone 13 Pro Max":
        if storage == "128 GB":
            print(42900)
        elif storage == "256 GB":
            print(46900)
        elif storage == "512 GB":
            print(54900)
        elif storage == "1 TB":
            print(62900)
        else:
            print("Not Available")

def main():
    """main"""
    model = input()
    storage = input()
    if model in "iPhone 13 mini":
        iphone13mini(model, storage)
    elif model in "iPhone 13":
        iphone13(model, storage)
    elif model in "iPhone 13 Pro":
        iphone13pro(model, storage)
    elif model in "iPhone 13 Pro Max":
        iphone13promax(model, storage)
    else:
        print("Not Available")
main()

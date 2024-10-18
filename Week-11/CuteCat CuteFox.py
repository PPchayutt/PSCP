"""CuteCat CuteFox"""
def compare_length(dict_cat, txt):
    """compare length"""
    return len([few for few in dict_cat.values() if txt in few])

def main():
    """main"""
    countable, dict_cat, cat_result = int(input()), {}, {}
    for _ in range(countable):
        txt = str(input())
        if len(txt.split('"')) > len(txt.split("'")):
            dict_cat[txt.split('"')[1]] = txt.split('"')[3]
        else:
            dict_cat[txt.split("'")[1]] = txt.split("'")[3]
    count_of_cat, count_of_fox = compare_length(dict_cat, "Cat"), compare_length(dict_cat, "Fox")
    check_of_cat, check_of_fox, count = "Cat01" in dict_cat.values(), \
        "Fox01" in dict_cat.values(), 0
    if not count_of_cat or not check_of_cat:
        cat_result["Garfield"] = "Cat01"
    if not count_of_fox or not check_of_fox:
        cat_result["Fubuki"] = "Fox01"
    for key, value in sorted(dict_cat.items(), key=lambda x: x[1]):
        if not check_of_fox and value.count("Fox") >= 1 and not count:
            count += 1
            cat_result["Fubuki"] = "Fox01"
        cat_result[key] = value
    count_of_cat, count_of_fox = compare_length(cat_result, "Cat"), \
        compare_length(cat_result, "Fox")
    cat, fox = {}, {}
    for key, value in cat_result.items():
        if value.count("Cat") >= 1:
            cat.update({int(value.split("Cat")[1]): [key, value]})
        elif value.count("Fox") >= 1:
            fox.update({int(value.split("Fox")[1]): [key, value]})
    print(f"Cat : {count_of_cat}\nFox : {count_of_fox}")
    for cry in sorted(cat):
        print(cat[cry][0] + " : " + cat[cry][1])
    for cry in sorted(fox):
        print(fox[cry][0] + " : " + fox[cry][1])
main()

"""Muddled Menu"""
def main():
    """main"""
    list_menu = []
    del_menu = []
    sort_list = []
    result = []
    while True:
        menu = input()
        if menu == "DONE":
            break
        if menu == "SOMETHING'S WRONG":
            list_menu.clear()
            continue
        if menu == "CLOSED":
            list_menu.clear()
            break
        if menu.startswith("Can't do: "):
            del_menu.append(menu[10:])
            continue
        list_menu.append(menu)
    for i in list_menu:
        location = i.find("#")
        locate = i[location+1:]
        if locate == "N":
            sort_list.append(i[:location-1])
        else:
            sort_list.insert(int(locate)-1,i[:location-1])
    for i in sort_list:
        if i not in del_menu:
            result.append(i)
    print(f"Full Course: {result} Reversed: {result[::-1]}")
main()

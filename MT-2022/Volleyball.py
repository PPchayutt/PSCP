"""volleyball"""
def comp(awin, bwin, val):
    """compare"""
    return awin >= val or bwin >= val

def tied(awin, bwin):
    """tied"""
    return abs(awin - bwin) >= 2

def volley(val, awin=0, bwin=0, teama=0, teamb=0):
    """volleybal"""
    string = ""
    add = 0
    end_game = False
    while len(val):
        for i in val:
            if (comp(awin, bwin, 25) and tied(awin, bwin) and add <= 3):
                end_game = True
                break
            if (comp(awin, bwin, 15) and tied(awin, bwin) and add == 4):
                end_game = True
                break
            if i == "A":
                awin += 1
            elif i == "B":
                bwin += 1
            string += i
        add += 1
        if awin > bwin:
            teama += 1
        else:
            teamb += 1
        if add <= 5:
            print(f"Set {add}: A ({awin}) | B ({bwin})")
        val = val.replace(string, "", 1)
        if add >= 4 and end_game and teama - teamb or (abs(teama - teamb) == 3):
            print(f"A won {teama}:{teamb} set" * (teama > teamb) +
                  f"B won {teamb}:{teama} set" * (teama < teamb))
            break
        end_game = False
        awin = 0
        bwin = 0
        string = ""
    if not end_game:
        print("The game has not finished yet.")
volley(input() + " ")

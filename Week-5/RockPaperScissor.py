"""RockPaperScissor"""
def main():
    """main"""
    rps = input()
    DRAW_A = 0
    DRAW_B = 0
    for i in range(0,len(rps),2):
        curr_match = rps[i:i+2]
        if curr_match == "RP":
            DRAW_B += 1
        elif curr_match == "SP":
            DRAW_A += 1
        elif curr_match == "PR":
            DRAW_A += 1
        elif curr_match == "PS":
            DRAW_B += 1
        elif curr_match == "RS":
            DRAW_A += 1
        elif curr_match == "SR":
            DRAW_B += 1
    if DRAW_A > DRAW_B:
        print(f"A win {DRAW_A}-{DRAW_B}")
    elif DRAW_A < DRAW_B:
        print(f"B win {DRAW_B}-{DRAW_A}")
    else:
        print(f"DRAW {DRAW_A}")
main()

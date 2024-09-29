"""Volleyball"""
def calculate_and_print_score(game_string):
    """calculate"""
    set_a, set_b = 0, 0
    score_a, score_b = 0, 0
    current_set = 1

    for point in game_string:
        if point == 'A':
            score_a += 1
        else:
            score_b += 1

        if current_set < 5:
            if (score_a >= 25 or score_b >= 25) and abs(score_a - score_b) >= 2:
                print(f"Set {current_set}: A ({score_a}) | B ({score_b})")
                if score_a > score_b:
                    set_a += 1
                else:
                    set_b += 1
                score_a, score_b = 0, 0
                current_set += 1
        else:
            if (score_a >= 15 or score_b >= 15) and abs(score_a - score_b) >= 2:
                print(f"Set {current_set}: A ({score_a}) | B ({score_b})")
                if score_a > score_b:
                    set_a += 1
                else:
                    set_b += 1
                break

    if score_a > 0 or score_b > 0:
        print(f"Set {current_set}: A ({score_a}) | B ({score_b})")

    if current_set < 5 and score_a == 0 and score_b == 0:
        print(f"Set {current_set}: A (0) | B (0)")

    if set_a == 3:
        print(f"A won {set_a}:{set_b} set")
    elif set_b == 3:
        print(f"B won {set_b}:{set_a} set")
    else:
        print("The game has not finished yet.")

game_string = input()

calculate_and_print_score(game_string)

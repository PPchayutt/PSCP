"""Game"""
def game(a_score, b_score):
    """game result"""
    if a_score % 3 == b_score % 3:
        print(a_score % 3)
    else:
        print("Error")
game(int(input()), int(input()))

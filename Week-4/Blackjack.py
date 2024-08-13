"""Blackjack"""
def main():
    """main"""
    num_card = int(input())
    total_point = 0
    ace_count = 0
    for _ in range(num_card):
        card = input()
        if card.isdigit():
            total_point += int(card)
        elif card in ("J", "Q", "K"):
            total_point += 10
        elif card == "A":
            ace_count += 1
    if ace_count > 0:
        if total_point + 11 + (ace_count - 1) > 21:
            total_point += ace_count
        else:
            total_point += 11 + (ace_count - 1)
    print(total_point)
main()

"""Nearer"""
def main(alice, bob, icecream):
    """main"""
    alice_range = abs(icecream - alice)
    bob_range = abs(icecream - bob)
    if alice_range < bob_range:
        print(f"Alice {alice_range}")
    elif bob_range < alice_range:
        print(f"Bob {bob_range}")
    else:
        print(f"Sundaes {bob_range}")
main(int(input()), int(input()), int(input()))

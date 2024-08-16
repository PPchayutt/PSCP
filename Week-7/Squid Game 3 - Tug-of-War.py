"""Squid Game 3 - Tug-of-War"""
def main():
    """Squid Game 3 - Tug-of-War"""
    totalA = 0
    totalB = 0
    for _ in range(10):
        teamA = int(input())
        totalA += teamA
    for _ in range(10):
        teamB = int(input())
        totalB += teamB
    if totalA < totalB:
        print("A")
    elif totalA > totalB:
        print("B")
    else:
        print("AB")
main()

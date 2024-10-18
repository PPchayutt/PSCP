"""Olympic"""
def main():
    """main"""
    numnation = int(input())
    nation = {}
    for _ in range(numnation):
        national = input().split()
        nation[national[0]] = tuple(map(int, national[1:]))
    sort_nation = sorted(nation.items(), key=lambda x: sum(x[1]), reverse=True)
    sort_nation.sort(key=lambda x: x[0])
    sort_nation.sort(key=lambda x: x[1], reverse=True)
    rank = 0
    now = 0
    old = 0
    for coun, score in sort_nation:
        sumscore = sum(score)
        score = " ".join(map(str, score))
        if score != old:
            rank += now
            now = 0
            rank += 1
        elif rank:
            now += 1
        print(rank, coun, score, sumscore)
        old = score
main()

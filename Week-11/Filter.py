"""Filter"""
import json
def main():
    """main"""
    omegadict = json.loads(input())
    score = float(input())
    result = []
    for i in omegadict:
        if omegadict[i] >= score:
            result.append(i)
    if not result:
        print("Nope")
    else:
        for i in sorted(result):
            print(f"{i}\t{omegadict[i]:.2f}")
main()

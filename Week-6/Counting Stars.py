"""Counting Stars"""
def main(sky):
    """main"""
    constellation_count = 0
    shootingstar_count = 0
    comet_count = 0
    i = 0
    while i < len(sky) - 1:
        if sky[i:i+2] == "**":
            constellation_count += 1
            i += 2
        elif sky[i:i+2] == "*/":
            shootingstar_count += 1
            i += 2
        elif sky[i:i+2] in ("~*", "*~"):
            comet_count += 1
            i += 2
        else:
            i += 1
    if (constellation_count or shootingstar_count or comet_count) > 0:
        print(f"constellation: {constellation_count}")
        print(f"comet: {comet_count}")
        print(f"shooting star: {shootingstar_count}")
    else:
        print("Tonight is a quiet night.")
main(input())

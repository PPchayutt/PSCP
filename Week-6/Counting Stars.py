"""Counting Stars"""
def main(sky):
    """main"""
    constellation_count = sky.count("**")
    shootingstar_count = sky.count("*/")
    comet_count = sky.count("~*") + sky.count("*~")
    if (not constellation_count) and (not comet_count) and (not shootingstar_count):
        print("Tonight is a quiet night.")
    else:
        print(f"constellation: {constellation_count}")
        print(f"comet: {comet_count}")
        print(f"shooting star: {shootingstar_count}")
main(input())

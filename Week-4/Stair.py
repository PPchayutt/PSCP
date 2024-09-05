"""Stair"""
def main(maxheight, steps):
    """main"""
    num_steps = 0
    current_height = 0
    for _ in range(steps):
        height = int(input())
        if height > maxheight:
            print("NO")
            return
        current_height += height
        if current_height > maxheight:
            num_steps += 1
            current_height = height
    if current_height > 0:
        num_steps += 1
    print(num_steps)
main(int(input()), int(input()))

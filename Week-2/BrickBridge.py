"""BrickBidge"""
def main():
    """Find a"""
    a = int(input())
    b = int(input())
    goal = int(input())
    max_big_bricks = goal // 5
    big_bricks = min(b, max_big_bricks)
    remaining_goal = goal - big_bricks * 5
    if remaining_goal <= a:
        print(remaining_goal)
    else:
        print(-1)
main()

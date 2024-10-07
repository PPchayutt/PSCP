"""Runner"""
def main():
    """main"""
    total_distance = int(input())
    n = int(input())
    best_time = -1
    winner = 0
    best_speed = 0
    for i in range(1, n + 1):
        speed, start_position = map(int, input().split())
        distance_to_run = total_distance - start_position
        if distance_to_run > 0:
            time = distance_to_run / speed
            if best_time == -1 or time < best_time or (time == best_time and speed > best_speed):
                best_time = time
                best_speed = speed
                winner = i
    print(winner)
main()

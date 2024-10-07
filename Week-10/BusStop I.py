"""BusStop I"""
def main(capacity, stops, passengers):
    """main"""
    bus = []
    total_arrived = 0
    for current_stop in range(1, stops + 1):
        bus = [p for p in bus if p != current_stop]
        for destination in passengers[current_stop]:
            if destination > current_stop and len(bus) < capacity:
                bus.append(destination)
                total_arrived += 1
            elif destination <= current_stop:
                continue
            else:
                break
    return total_arrived

def get_passenger_data(num_stops):
    """return passenger data"""
    passengers = {i: [] for i in range(1, num_stops + 1)}
    for i in range(num_stops):
        stop_info = list(map(int, input().split()))
        stop_number = stop_info[0]
        passengers[stop_number] = stop_info[1:]
    return passengers
CAPACITY = int(input())
NUM_STOPS = int(input())
PASSENGERS = get_passenger_data(NUM_STOPS)
RESULT = main(CAPACITY, NUM_STOPS, PASSENGERS)
print(RESULT)

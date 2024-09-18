def extract_ip(line):
    start = line.find('[') + 1
    end = line.find(']')
    return line[start:end]

def extract_time(line):
    if 'time=' in line:
        start = line.find('time=') + 5
        end = line.find('ms', start)
        return int(line[start:end])
    elif 'time<1ms' in line:
        return 0
    return -1

def calculate_statistics(inputs):
    ip_address = extract_ip(inputs[1])
    sent = 4
    received = 0
    lost = 0
    min_time = float('inf')
    max_time = 0
    total_time = 0

    for i in range(2, 6):
        time = extract_time(inputs[i])
        if time >= 0:
            received += 1
            total_time += time
            if time < min_time:
                min_time = time
            if time > max_time:
                max_time = time
        else:
            lost += 1

    loss_percentage = (lost * 100) // sent
    avg_time = total_time // received if received > 0 else 0

    if received == 0:
        min_time = max_time = 0

    return (ip_address, sent, received, lost, loss_percentage, min_time, max_time, avg_time)

# Read input
inputs = [''] * 7
for i in range(7):
    inputs[i] = input()

# Calculate statistics
stats = calculate_statistics(inputs)

# Print output
print(f"Ping statistics for {stats[0]}:")
print(f"    Packets: Sent = {stats[1]}, Received = {stats[2]}, Lost = {stats[3]} ({stats[4]}% loss),")
if stats[2] > 0:
    print("Approximate round trip times in milli-seconds:")
    print(f"    Minimum = {stats[5]}ms, Maximum = {stats[6]}ms, Average = {stats[7]}ms")
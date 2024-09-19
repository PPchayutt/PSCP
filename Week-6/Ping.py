"""Ping"""
def find_ip(x):
    """Find IP address"""
    index_stop = x.find("with") - 2
    index_start, temp_var = index_stop, x[index_stop]
    while not temp_var.isspace():
        index_start -= 1
        temp_var = x[index_start]
    return x[index_start:index_stop + 1].replace("[", "").replace("]", "").strip()
def find_time(x):
    """Find reply time"""
    if x.find("time<1") != -1:
        return 0
    if x.find("time=") != -1:
        index_start = x.find("time=") + 5
        index_stop, temp_var = index_start, x[index_start]
        while temp_var != "s":
            index_stop += 1
            temp_var = x[index_stop]
        return int(x[index_start:index_stop + 1].replace("m", "").replace("s", "").strip())
    return None
def get_ping(sent, receive):
    """Get the ping value"""
    sent, receive = 4, 0
    line = [input(), input(), input(), input(), input()]
    time = [None, None, None, None]
    ip_address = find_ip(line[0])
    for i in range(1, 5):
        x = find_time(line[i])
        time[i-1] = x
        receive += 1 if x is not None else 0
    print(f"Ping statistics for {ip_address}:")
    if not receive:
        print("    Packets: Sent = 4, Received = 0, Lost = 4 (100% loss),")
    else:
        ping_lowest = time[0] if time[0] is not None else time[1] if time[1] is not None else \
                        time[2] if time[2] is not None else time[3]
        ping_hightest = ping_lowest
        ping_avg = 0
        for i in range(4):
            if str(time[i]).isnumeric():
                ping_lowest = time[i] if ping_lowest > time[i] else ping_lowest
                ping_hightest = time[i] if ping_hightest < time[i] else ping_hightest
                ping_avg += time[i]
        print(f"    Packets: Sent = 4, Received = {receive}, \
Lost = {sent-receive} ({int((sent-receive)/sent*100)}% loss),")
        print("Approximate round trip times in milli-seconds:")
        print(f"    Minimum = {ping_lowest}ms, Maximum = {ping_hightest}ms, \
Average = {int(ping_avg/receive)}ms")
get_ping(input(), input())

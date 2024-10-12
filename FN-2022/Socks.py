"""Socks"""
def count_socks(socks):
    """count socks"""
    sock_count = {}
    for sock in socks:
        if sock in sock_count:
            sock_count[sock] += 1
        else:
            sock_count[sock] = 1
    return sock_count

def sort_socks(socks):
    """sort socks"""
    sock_count = count_socks(socks)
    paired_socks = []
    total_pairs = 0
    for sock in sorted(sock_count.keys()):
        count = sock_count[sock]
        pairs = count // 2
        if pairs > 0:
            paired_socks.extend([sock * 2] * pairs)
            total_pairs += pairs
    result = " ".join(paired_socks) if paired_socks else "None"
    return result, total_pairs
socks_input = input().strip()
sorted_socks, pair_count = sort_socks(socks_input)
print(sorted_socks)
print(pair_count)

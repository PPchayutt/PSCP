"""Duplicate I"""
def main():
    """main"""
    n_set = set()
    m_set = set()
    n_count = int(input())
    m_count = int(input())
    for _ in range(n_count):
        n = int(input())
        n_set.add(n)
    for _ in range(m_count):
        m = int(input())
        m_set.add(m)
    o = n_set.intersection(m_set)
    o_sort = sorted(o, reverse=True)
    if not o_sort:
        print("Nope")
    else:
        for i in o_sort:
            print(i)
main()

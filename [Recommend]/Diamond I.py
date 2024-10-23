"""Diamond I"""
def calculate_max_diamond_value(diamond_field, n):
    """calculate function"""
    if not diamond_field or not diamond_field[0]:
        return 0
    m = len(diamond_field)
    column_sums = [sum(diamond_field[i][j] for i in range(m)) for j in range(n)]
    return max(column_sums)

def main():
    """main"""
    m = int(input())
    n = int(input())
    diamond_field = []
    for _ in range(m):
        row = list(map(int, input().split()))
        diamond_field.append(row)
    result = calculate_max_diamond_value(diamond_field, n)
    print(result)
main()

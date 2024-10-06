"""Point Sorting"""
def sort_points(points):
    """sort the points"""
    return sorted(points, key=lambda p: (p[0] + p[1], -p[1]))

def main():
    """main"""
    t = int(input())
    for _ in range(t):
        n = int(input())
        points = []
        for _ in range(n):
            x, y = map(int, input().split())
            points.append((x, y))
        sorted_points = sort_points(points)
        for x, y in sorted_points:
            print(x, y)
main()

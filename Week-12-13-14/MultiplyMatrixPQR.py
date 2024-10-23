"""MultiplyMatrixPQR"""
def main():
    """main"""
    p = int(input())
    q = int(input())
    r = int(input())
    a = []
    for _ in range(p):
        row = []
        for _ in range(q):
            row.append(int(input()))
        a.append(row)
    b = []
    for _ in range(q):
        row = []
        for _ in range(r):
            row.append(int(input()))
        b.append(row)
    c = [[0] * r for _ in range(p)]
    for i in range(p):
        for j in range(r):
            c[i][j] = sum(a[i][k] * b[k][j] for k in range(q))
    for row in c:
        print(*row)
main()

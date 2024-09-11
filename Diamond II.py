"""Diamond II"""
def minediamondd(n, m):
    """diamondd"""
    diamonds = []
    for _ in range(m):
        diamonds.append(list(map(int, input().split())))
    dp = [[0] * n for _ in range(m)]
    for j in range(n):
        dp[0][j] = diamonds[0][j]
    for i in range(1, m):
        for j in range(n):
            max_val = dp[i-1][j]
            if j > 0:
                max_val = max(max_val, dp[i-1][j-1])
            if j < n - 1:
                max_val = max(max_val, dp[i-1][j+1])
            dp[i][j] = diamonds[i][j] + max_val
    max_diamond = max(dp[m-1])
    print(max_diamond)
minediamondd(int(input()), int(input()))

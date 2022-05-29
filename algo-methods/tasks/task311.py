N, M = map(int, input().split())
nums = [0] + list(map(int, input().split()))

inf = 2 ** 30

dp = [[inf] * (M+1) for i in range(N+1)]
dp[0][0] = 0

for i in range(1, N+1):
    for m in range(1, M+1):
        num = nums[i]
        dp[i][m] = min(dp[i-1][m], dp[i][m])
        if m >= num:
            dp[i][m] = min(dp[i-1][m - num] + 1, dp[i][m])

if dp[N][M] == inf:
    dp[N][M] = -1
print(dp[N][M])

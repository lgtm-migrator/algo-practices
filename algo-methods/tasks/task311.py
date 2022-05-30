N, M = map(int, input().split())
nums = [0] + list(map(int, input().split()))

inf = 2 ** 30

dp = [[inf] * (M+1) for i in range(N+1)]
dp[0][0] = 0

for i in range(0, N):
    for m in range(0, M+1):
        num = nums[i]
        dp[i+1][m] = min(dp[i][m], dp[i+1][m])
        if m >= num:
            dp[i+1][m] = min(dp[i][m - num] + 1, dp[i+1][m])

if dp[N][M] == inf:
    dp[N][M] = -1
print(dp[N][M])

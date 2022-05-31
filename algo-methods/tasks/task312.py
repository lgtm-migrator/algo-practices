N, M, K = map(int, input().split())

nums = list(map(int, input().split()))

inf = 2 ** 30

# dp[i][m][k]だと計算量がO(NMK)になる
dp = [[inf] * (M+1) for i in range(N+1)]
dp[0][0] = 0

for i in range(N):
    num = nums[i]
    for m in range(0, M+1):
        cap = m - num
        if cap >= 0:
            dp[i+1][m] = min(dp[i][cap] + 1, dp[i][m])
        else:
            dp[i+1][m] = dp[i][m]

if dp[N][M] <= K:
    print("Yes")
else:
    print("No")

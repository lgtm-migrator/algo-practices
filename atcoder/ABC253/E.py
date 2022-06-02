from itertools import accumulate

N, M, K = map(int, input().split())
mod = 998244353

dp = [[0] * (1+M) for i in range(1+N)]
for j in range(1, M+1):
    dp[1][j] = 1

for i in range(1, N):
    # 事前に累積和を考えておく
    prev = list(accumulate(dp[i]))
    for j in range(1, M+1):
        result = 0
        if K == 0:
            result = prev[M]
        else:
            if j - K > 0:
                result += prev[j - K] - prev[0]
            if j+K <= M:
                result += prev[M] - prev[j+K-1]
        # 細かくmodで割っていかないとaccumulateした時にオーバーフローしてしまう
        dp[i+1][j] = result % mod


ans = sum(dp[N]) % mod

print(ans)

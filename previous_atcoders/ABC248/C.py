from typing import List

N, M, K = map(int, input().split())

# dp[i][j]...i番目までの数を決定して総和がjになる場合の数列の個数
# dp[0][0]...どの数字も選ばない場合、総和は0で1通りを満たす
dp: List[List[int]] = [[0] * (K+1) for i in range(N+1)]
dp[0][0] = 1

# i番目まで数字が確定している
for i in range(N):
    # jは前までの総和
    for j in range(0, K):
        # mは今回選ぶ数字
        for m in range(1, M+1):
            if j + m > K:
                continue
            dp[i+1][j+m] += dp[i][j]

ret = 0
for k in range(1, K+1):
    ret += dp[N][k]

print(ret % 998244353)

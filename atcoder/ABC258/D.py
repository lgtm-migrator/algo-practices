N, X = map(int, input().split())
A = []
B = []

for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

INF = 2 ** 60

# B_min_acc[i]...i番目までの中で最小のB
B_min_acc = []
for bi in B:
    if len(B_min_acc) == 0:
        B_min_acc.append(bi)
        continue
    B_min_acc.append(min(bi, B_min_acc[-1]))

dp = [INF for j in range(N)]
dp[0] = A[0] + B[0]

for i in range(1, N):
    dp[i] = dp[i-1] + A[i] + B[i]

best = INF

for i, (pre, rep) in enumerate(zip(dp, B_min_acc)):
    remain_count = X - (i+1)
    add = remain_count * B_min_acc[i]
    best = min(pre + add, best)

print(best)

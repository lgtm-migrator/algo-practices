N, K = map(int, input().split())
s = input()
characters = [c for c in s]

dp = [[2 ** 60] * N for j in range(K)]


# K回の操作
for k in range(0, K):
    kinds = set(characters)
    # j番目の文字を変える
    for j in range(0, N):
        max_eval = 0
        for kind in kinds:
            if kind == characters[j]:
                continue
            s = characters[:j] + [kind] + characters[j+1:]
            head = s[:len(s)//2]
            tail = s[len(s)//2:]
            eval = 0
            for h, t in zip(head, tail):
                if h == t:
                    eval += 1
            if eval > max_eval:
                max_eval = eval
        dp[k][j] = min(dp[k][j-1], dp[])


print(dp[K-1][N-1])

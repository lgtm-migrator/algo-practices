N = int(input())
S = list(map(str, input()))

# Rの位置を把握する
v = 0
size = 0
for i, c in enumerate(S):
    if i == 0 or i == N - 1:
        continue
    if c == "R":
        l = i-1
        find = False
        while l >= 0 and S[l] == "A":
            l -= 1
            find = True
        r = i+1
        while r < N and S[r] == "C":
            r += 1
            find = True
        v += min(i - (l + 1), (r - 1) - i)
        size += 1 if find else 0

ans = min(v, 2 * size)

print(ans)

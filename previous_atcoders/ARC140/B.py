N = int(input())
S = list(map(str, input()))

# Rの位置を把握する
rlist = []
for i, c in enumerate(S):
    if i == 0 or i == N - 1:
        continue
    if c == "R":
        l = i-1
        while l >= 0 and S[l] == "A":
            l -= 1
        r = i+1
        while r < N and S[r] == "C":
            r += 1
        r = min(i - (l + 1), (r - 1) - i)
        rlist.append(r)

ans = min(sum(rlist), 2 * len(rlist))

print(ans)

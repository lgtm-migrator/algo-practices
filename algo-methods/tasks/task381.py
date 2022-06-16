N, K = map(int, input().split())

A = sorted(list(map(int, input().split())))

ans = 0

for i in range(N):
    ai = A[i]
    l = 0
    r = N
    while l != r:
        mid = (r + l) // 2
        if A[mid] >= K - ai:
            r = mid
        else:
            l = mid + 1
    ans += N - r

print(ans)

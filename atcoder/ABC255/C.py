X, A, D, N = map(int, input().split())

if D == 0:
    print(abs(X - A))
    exit()

if D < 0:
    # Dが負の場合は配列を反転させる
    last = A + (N - 1) * D
    D *= -1
    A = last

# Sの配列を用意する必要はない

l = 0
r = N+1
while r - l != 1:
    mid = l + (r - l) // 2
    val = A + (mid - 1) * D
    if val < X:
        l = mid
    else:
        r = mid


if r > N:
    print(X - (A + (l - 1) * D))
    exit()
elif l < 1:
    print((A + (r - 1) * D) - X)
    exit()
first = A + (l - 1) * D
second = A + (r - 1) * D
ans = min(X - first, second - X)
print(ans)

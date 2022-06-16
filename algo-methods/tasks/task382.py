N, M = map(int, input().split())

A = sorted(list(map(int, input().split())))
B = list(map(int, input().split()))

for k in range(M):
    b = B[k]
    l = 0
    r = N
    while r - l != 0:
        mid = (l + r) // 2
        if A[mid] > b:
            r = mid
        else:
            l = mid+1
    print(r)

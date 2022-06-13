N, M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))


for k in range(M):
    l = 0
    r = N-1
    while r - l != 0:
        mid = (l + r) // 2
        if A[mid] >= B[k]:
            r = mid
        else:
            l = mid+1
    print(r)

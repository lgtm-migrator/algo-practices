N, L = map(int, input().split())
K = int(input())

separators = list(map(int, input().split()))

# (K+1)以上のピースに分割した。その時、全てのピースの長さがM以上である
# →Mがスコア。Mは最大でもLなので二分探索で（O(logL)）で解ける

l = -1
r = L+1

while r - l > 1:
    m = (r + l) // 2
    k = 0
    prev = 0
    for j in range(N):
        length = separators[j] - prev
        if length >= m and L - separators[j] >= m:
            k += 1
            prev = separators[j]
    if k >= K:
        l = m
    else:
        r = m

print(l)

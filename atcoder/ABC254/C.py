N, K = map(int, input().split())

nums = list(map(int, input().split()))

inf = 2 ** 60

threshold = [-1 for i in range(N)]

G = []

can = True

called = set()

for i in range(N-K):
    if i in called:
        continue
    cur = i
    group = []
    while cur < N:
        called.add(cur)
        group.append(nums[cur])
        cur += K
    G.append(group)


if K >= N-K:
    for i in range(N-K, K):
        if i not in called:
            G.append([nums[i]])


for g in G:
    g = sorted(g)

    for num, th in zip(g, threshold):
        if num < th:
            can = False
            break
    else:
        threshold = g


if can:
    print("Yes")
else:
    print("No")

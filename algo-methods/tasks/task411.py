N, A, B = map(int, input().split())
G = [set() for i in range(N)]
for i in range(N):
    s = list(map(str, input()))
    for j, c in enumerate(s):
        if c == "o":
            G[i].add(j)
            G[j].add(i)

friends = G[A]
if B in friends:
    print("Yes")
else:
    print("No")

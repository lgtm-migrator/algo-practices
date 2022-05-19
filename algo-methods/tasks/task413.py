N, M, X = map(int, input().split(" "))
graph = [[] for i in range(N)]
for i in range(M):
    A, B = map(int, input().split(" "))
    graph[A].append(B)
    graph[B].append(A)

ans = set()

for f in graph[X]:
    for ff in graph[f]:
        if ff in graph[X] or ff == X:
            continue
        ans.add(ff)

print(len(ans))

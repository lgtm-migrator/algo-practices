N, M = map(int, input().split())

graph = [[] for i in range(N)]

for i in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

best = []
for friends in graph:
    if len(best) < len(friends):
        best = friends

for i, friend in enumerate(sorted(best)):
    print(friend, end="" if i == len(best)-1 else " ")

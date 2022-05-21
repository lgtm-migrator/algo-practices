from queue import Queue

N, M = map(int, input().split())

graph = [[] for i in range(N)]

for i in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

# 各頂点が何手目で探索されたか
dist = [-1] * N
# k手目に探索された頂点集合を格納
nodes = [[] for i in range(N)]

# 初期化
dist[0] = 0
nodes[0] = [0]

# k手目の探索をする
for k in range(1, N):
    for v in nodes[k-1]:
        for n in graph[v]:
            # nはk手目で届く頂点
            if dist[n] != -1:
                # 既に探索済みであるため、最短を保持したくコンティニュー
                continue
            # 探索済みにする
            # 探索ずみ...nodesのどこかしらの要素に頂点が格納されている && dist[v]が-1ではない
            dist[n] = dist[v] + 1
            nodes[k].append(n)

for k in range(N):
    nodes[k].sort()

    print(*nodes[k])

import sys
sys.setrecursionlimit(10**6)


N = int(input())
roots = map(int, input().split())
graph = [[] for i in range(N)]

for i, root in enumerate(roots):
    graph[root].append(i+1)


# 子供を根とした部分木の個数が先にほしいため、「行きかけ順」ではなく「帰りがけ順」にする
def rec(vertex, size, graph):
    # 帰りかけ順は先に再起関数を呼ぶ
    for child in graph[vertex]:
        rec(child, size, graph)

    size[vertex] = 1
    for child in graph[vertex]:
        size[vertex] += size[child]


# 木の根から再帰的に探索
size = [0] * N
rec(0, size, graph)

for s in size:
    print(s-1)

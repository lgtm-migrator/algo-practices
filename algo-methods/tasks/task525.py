import sys
sys.setrecursionlimit(10 ** 6)

N = int(input())
graph = [[] for i in range(N)]

ps = map(int, input().split())

for i, p in enumerate(ps):
    graph[p].append(i+1)


ans = []


# 頂点rootを根とする部分期を探索
def rec(root, graph):
    ans.append(root)
    for child in graph[root]:
        rec(child, graph)


rec(0, graph)

for a in ans:
    print(a, end=" ")

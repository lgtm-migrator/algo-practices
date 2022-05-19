import sys
sys.setrecursionlimit(10 ** 6)

N = int(input())

graph = [[] for i in range(N)]
roots = list(map(int, input().split()))

for i, root in enumerate(roots):
    graph[root].append(i+1)

best = 0

depth = [0] * N


def rec(root, depth, graph):
    children = graph[root]
    for child in children:
        depth[child] = depth[root] + 1
        rec(child, depth, graph)


rec(0, depth, graph)

print(max(depth))

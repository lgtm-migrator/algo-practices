import sys
sys.setrecursionlimit(10 ** 6)


N = int(input())
# 親を知っていれば子供にアクセスできるデータ構造にする
graph = [[] for i in range(N)]
nums = list(map(int, input().split()))

for i in range(1, N):
    parent = nums[i-1]
    graph[parent].append(i)


# 親に対して子供を見つける
def rec(vertex, depth, graph):
    """
    :param int vertex: 根（部分木の根も可能）
    :param int depth: 深さ配列
    :param List[List[int]] graph: グラフデータ
    """
    children = graph[vertex]
    for child in children:
        depth[child] += depth[vertex] + 1
        rec(child, depth, graph)


depth = [0] * N

rec(0, depth, graph)

for d in depth:
    print(d)

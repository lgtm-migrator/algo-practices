from typing import List
from queue import Queue

Graph = List[List[int]]


class Solution:
    def bfs(self, graph: Graph, start: int) -> List[int]:
        size = len(graph)
        distances = [-1] * size
        que = Queue()
        distances[0] = 0
        # 最初の点を橙色にする
        que.put(0)
        while not que.empty():
            vertex = que.get()
            for v in graph[vertex]:
                if distances[v] != -1:
                    # 既に探索されているためスキップする
                    continue
                distances[v] = distances[vertex] + 1
                que.put(v)

        return distances


if __name__ == "__main__":
    N, M = map(int, input().split())
    graph: Graph = [[] * N for i in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a] += [b]
        # 無向グラフなので
        graph[b] += [a]

    sol = Solution()
    distances = sol.bfs(graph, 0)

    # 結果の出力
    for v in range(N):
        print(f"{v}: {distances[v]}")

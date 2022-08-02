from collections import defaultdict
from typing import Generic, Iterable, Iterator, Optional, TypeVar, Union, List
import datetime
import re
from bisect import bisect_left, bisect_right
import random
import heapq
from queue import PriorityQueue
from collections import Counter
import itertools
from collections import deque
import math
import decimal
import sys

sys.setrecursionlimit(10**9)

INF = 2 << 60
MOD = 998244353


N, M = map(int, input().split())

graph: List[List[int]] = [[] for j in range(N)]
reverse_graph: List[List[int]] = [[] for j in range(N)]
find_index_list: List[int] = []

for i in range(M):
    a, b = map(lambda num: int(num) - 1, input().split())
    graph[a].append(b)
    reverse_graph[b].append(a)


# DFS（帰りかけ順）
seen = [False for i in range(N)]


def step1(node: int):
    seen[node] = True
    for nxt in graph[node]:
        if seen[nxt]:
            continue
        step1(nxt)
    find_index_list.append(node)


for i in range(N):
    if seen[i]:
        continue
    step1(i)

# print(seen)
# print(graph)
# print(reverse_graph)
# print(find_index_list)


def step2() -> int:
    cnt = 0
    seen = [False for i in range(N)]
    find_index_list.reverse()

    g = []

    def dfs(node: int):
        seen[node] = True
        g.append(node)
        for nxt in reverse_graph[node]:
            if seen[nxt]:
                continue
            dfs(nxt)

    for index in find_index_list:
        if seen[index]:
            continue
        dfs(index)
        lg = len(g)
        cnt += lg * (lg-1) // 2
        g = []
    return cnt


cnt = step2()

print(cnt)

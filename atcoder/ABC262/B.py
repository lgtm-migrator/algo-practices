from collections import defaultdict
from typing import Generic, Iterable, Iterator, TypeVar, Union, List
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

sys.setrecursionlimit(10**6)

INF = 2 << 60
MOD = 998244353


N, M = map(int, input().split())

graph = [[] for j in range(N+1)]

for i in range(M):
    u, v = map(int, input().split())
    graph[v].append(u)
    graph[u].append(v)

ans = 0

for a in range(1, N+1):
    for b in range(a+1, N+1):
        for c in range(b+1, N+1):
            if b in graph[a] and b in graph[c] and c in graph[a]:
                ans += 1

print(ans)

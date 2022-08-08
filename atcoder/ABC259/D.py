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
# 文字列を入力する場合は改行が残る
input = sys.stdin.readline
# 文字列を入力する場合
# input_str = input()[:-1]

INF = 2 << 60
MOD = 998244353

N = int(input())
sx, sy, tx, ty = map(int, input().split())


class Circle:
    def __init__(self, x: int, y: int, r: int):
        self.x = x
        self.y = y
        self.r = r

    def isIntersect(self, other) -> bool:
        origin_diff = (self.x - other.x) ** 2 + (self.y - other.y) ** 2
        if origin_diff + min(self.r, other.r) < max(self.r, other.r):
            # 内側に隠れている
            return (self.r + other.r) ** 2 <= origin_diff
        return (self.r + other.r) ** 2 >= origin_diff


circles: List[Circle] = []

for i in range(N):
    x, y, t = map(int, input().split())
    circles.append(Circle(x, y, t))

G = [[] for i in range(N)]

source_indexes = []
target_indexes = []

for i in range(N):
    circle = circles[i]

    if (sx - circle.x) ** 2 + (sy - circle.y) ** 2 == circle.r ** 2:
        source_indexes.append(i)

    if (tx - circle.x) ** 2 + (ty - circle.y) ** 2 == circle.r ** 2:
        target_indexes.append(i)

    for j in range(i):
        other = circles[j]
        if circle.isIntersect(other):
            G[i].append(j)
            G[j].append(i)

seen = [False for i in range(N)]


def dfs(index: int):
    for nxt in G[index]:
        if seen[nxt]:
            continue
        seen[nxt] = True
        dfs(nxt)


for start in source_indexes:

    if seen[start]:
        continue

    seen[start] = True
    dfs(start)

can = False

for target in target_indexes:
    if seen[target]:
        can = True
        break

# print(G)
# print(seen)

print("Yes" if can else "No")

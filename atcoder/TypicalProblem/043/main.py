from collections import defaultdict
from typing import Deque, Generic, Iterable, Iterator, TypeVar, Union, List
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

H, W = map(int, input().split())
rs, cs = map(int, input().split())
rt, ct = map(int, input().split())
rs -= 1
cs -= 1
rt -= 1
ct -= 1

S: List[List[int]] = [[] for i in range(H)]

for i in range(H):
    rows = list(map(str, input()[:-1]))
    for row in rows:
        if row == ".":
            S[i].append(1)
        else:
            S[i].append(0)


# dist[i][j][k]...(i, j)の点に向きkより向かうときの最小の曲がり回数
dist: List[List[List[int]]] = [
    [[INF for k in range(4)] for j in range(W)] for i in range(H)]

dxs = [0, 0, 1, -1]
dys = [-1, 1, 0, 0]


class State:
    def __init__(self, x: int, y: int, direction: int):
        self.x = x
        self.y = y
        self.direction = direction


que: Deque[State] = deque([])

for i in range(4):
    dist[rs][cs][i] = 0
    que.append(State(rs, cs, i))


while len(que) > 0:
    front = que.popleft()
    for dx, dy, dir in zip(dxs, dys, range(4)):
        nx, ny = front.x + dx, front.y + dy
        cost = 1 if front.direction != dir else 0
        if nx < 0 or nx >= H or ny < 0 or ny >= W:
            continue
        if not S[nx][ny] or cost + dist[front.x][front.y][front.direction] >= dist[nx][ny][dir]:
            continue
        newState = State(nx, ny, dir)
        dist[nx][ny][dir] = cost + dist[front.x][front.y][front.direction]
        if cost == 0:
            que.appendleft(newState)
        else:
            que.append(newState)

ans = INF

# print(dist)

for i in range(4):
    ans = min(ans, dist[rt][ct][i])

print(ans)

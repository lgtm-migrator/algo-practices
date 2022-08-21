from collections import defaultdict
from optparse import Option
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

sys.setrecursionlimit(10**6)
# 文字列を入力する場合は改行が残る
input = sys.stdin.readline
# 文字列を入力する場合
# input_str = input()[:-1]

INF = 2 << 60
MOD = 998244353

H, W = map(int, input().split())

# roles[y][x]でy,xのロール
roles = [[None for j in range(W+1)] for i in range(H+1)]

fields: List[List] = [[None for i in range(W+1)] for j in range(H+1)]


class Point:
    def __init__(self, y: int, x: int, role: str):
        self.y = y
        self.x = x
        self.role = role
        self.destination = None
        self.paths = []

    def __eq__(self, __o: object) -> bool:
        return self.x == __o.x and self.y == __o.y

    def can_enter(self) -> bool:
        global H, W
        if self.y == H and self.role == "D":
            return False
        if self.y == 1 and self.role == "U":
            return False
        if self.x == 1 and self.role == "L":
            return False
        if self.x == W and self.role == "R":
            return False
        return True

    def enter(self):
        if self.role == "D":
            return Point(self.y + 1, self.x, roles[self.y + 1][self.x])
        elif self.role == "U":
            return Point(self.y - 1, self.x, roles[self.y - 1][self.x])
        elif self.role == "L":
            return Point(self.y, self.x - 1, roles[self.y][self.x - 1])
        elif self.role == "R":
            return Point(self.y, self.x + 1, roles[self.y][self.x + 1])
        raise NotImplementedError()


for i in range(1, H+1):
    roles[i][1:] = list(map(str, input()[:-1]))

for i in range(1, H+1):
    for j in range(1, W+1):
        cur = Point(i, j, roles[i][j])
        origin = cur.role
        if cur.can_enter():
            nxt = cur.enter()
            if nxt.can_enter():
                cur.destination = nxt
            while nxt.can_enter() and nxt.role == cur.role:
                cur.paths.append(nxt)
                if nxt.can_enter() and nxt.role == cur.role:
                    cur.destination = nxt
                nxt = nxt.enter()

        fields[i][j] = cur

cur = fields[1][1]
seen = []

loop = False

while cur.can_enter():
    # print(cur.x, cur.y)
    if cur in seen:
        loop = True
        break
    seen.append(cur)
    if cur.can_enter():
        cur = cur.destination
        seen.extend(cur.paths)
    else:
        break

if loop:
    print(-1)
else:
    print(cur.y, cur.x)

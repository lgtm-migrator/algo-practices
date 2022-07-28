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


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())


H, W = map(int, input().split())
Q = int(input())
q = []

red_union_find = UnionFind(H*W)
board = [False for i in range(H*W+1)]

inputs_list = []

for i in range(Q):
    inputs_list.append(list(map(int, input().split())))

for inputs in inputs_list:
    t = inputs[0]
    if t == 1:
        r, c = inputs[1:]
        id = (r-1) * W + (c - 1)
        board[id] = True
        dxs = [-1, 0, 1, 0]
        dys = [0, 1, 0, -1]
        for dx, dy in zip(dxs, dys):
            nr = r + dy
            nc = c + dx
            if nr >= 1 and nr <= H and nc >= 1 and nc <= W:
                n_id = (nr - 1) * W + (nc - 1)
                if not board[n_id]:
                    continue
                red_union_find.union(id, n_id)
    elif t == 2:
        ra, ca, rb, cb = inputs[1:]
        id_a = (ra - 1) * W + (ca - 1)
        id_b = (rb - 1) * W + (cb - 1)
        if red_union_find.same(id_a, id_b) and board[id_a] == board[id_b] == True:
            print("Yes")
        else:
            print("No")

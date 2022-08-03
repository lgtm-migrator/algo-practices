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
G = [[] for i in range(N)]

for i in range(N-1):
    a, b = map(lambda num: int(num) - 1, input().split())
    G[a].append(b)
    G[b].append(a)

G1 = []
G2 = []

colors = [-1] * N

# 再起使う時はpypyよりpython使う


def dfs(pos: int, color: int):
    """
    @param color: 0 or 1
    """
    colors[pos] = color
    if color == 0:
        G1.append(pos)
    elif color == 1:
        G2.append(pos)
    for nxt in G[pos]:
        if colors[nxt] != -1:
            continue
        dfs(nxt, 1 - color)


dfs(0, 0)

if len(G1) >= len(G2):
    for num in G1[:N//2]:
        print(num+1, end=" ")
else:
    for num in G2[:N//2]:
        print(num+1, end=" ")
print("")

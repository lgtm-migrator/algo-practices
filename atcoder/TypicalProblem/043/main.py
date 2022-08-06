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

H, W = map(lambda num: int(num) - 1, input().split())
rs, cs = map(lambda num: int(num) - 1, input().split())
rt, ct = map(lambda num: int(num) - 1, input().split())


G: List[List[List[int]]] = [[[] for j in range(W+1)] for i in range(H+1)]

dxs = [0, 0, 1, -1]
dys = [-1, 1, 0, 0]

for i in range(H):
    rows = list(map(str, input()[:-1]))
    for j, area in enumerate(rows):
        if area == ".":
            G[i][j].append()

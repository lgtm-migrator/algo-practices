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

N, Q = map(int, input().split())

A = list(map(int, input().split()))

# 要素数: N-1個
B = []

for i in range(1, N):
    B.append(A[i] - A[i-1])

L = []
R = []
V = []

for i in range(Q):
    l, r, v = map(int, input().split())
    L.append(l)
    R.append(r)
    V.append(v)

ans = sum(list(map(abs, B)))

for l, r, v in zip(L, R, V):
    prev = 0
    cur = 0
    if l-2 >= 0:
        prev += abs(B[l-2])
        B[l-2] += v
        cur += abs(B[l-2])
    if r-1 < N-1:
        prev += abs(B[r-1])
        B[r-1] -= v
        cur += abs(B[r-1])
    ans += cur - prev
    print(ans)

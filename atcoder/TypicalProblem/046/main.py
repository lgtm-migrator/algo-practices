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
MOD = 46

N = int(input())

A = list(map(lambda i: int(i) % MOD, input().split()))
B = list(map(lambda i: int(i) % MOD, input().split()))
C = list(map(lambda i: int(i) % MOD, input().split()))

A_map = defaultdict(int)
B_map = defaultdict(int)
C_map = defaultdict(int)

for ai in A:
    A_map[ai] += 1

for bi in B:
    B_map[bi] += 1

for ci in C:
    C_map[ci] += 1

ans = 0

for i in range(MOD):
    for j in range(MOD):
        a, b = A_map[i], B_map[j]
        k = (MOD - (i + j) % MOD) % MOD
        c = C_map[k]
        val = a * b * c
        ans += val

print(ans)

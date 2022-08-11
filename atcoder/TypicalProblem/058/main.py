from collections import defaultdict
from difflib import diff_bytes
from typing import Generic, Iterable, Iterator, Tuple, TypeVar, Union, List
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
MOD = 100_000

N, K = map(int, input().split())

G: List[int] = [-INF for i in range(100_000)]

for i in range(100_000):
    num = i
    for digit in list(map(int, str(i))):
        num += digit
    num %= MOD
    G[i] = num

# key: num, value: find time
seen = dict()


def rec_end(num: int, cnt: int):
    if cnt == 0:
        print(num)
        return
    rec_end(G[num], cnt-1)


def rec(num: int, cnt: int):
    if cnt == K:
        print(num)
        return
    seen[num] = cnt
    nxt = G[num]
    if nxt in seen.keys():
        cycle_length = cnt - seen[nxt] + 1
        head_length = seen[nxt]
        pos = (K - head_length) % cycle_length
        rec_end(nxt, pos)
    else:
        rec(nxt, cnt+1)


rec(N, 0)

# print(seen)

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

S = list(map(str, input()[:-1]))
T = list(map(str, input()[:-1]))

sl = len(S)
tl = len(T)

cur = ""
cnt = 0

can = True

S_groups = []
T_groups = []

for c in S:
    if c == cur:
        cnt += 1
        S_groups[-1] = (cur, cnt)
    else:
        cnt = 1
        cur = c
        S_groups.append((cur, cnt))

cur = ""
cnt = 0

for c in T:
    if c == cur:
        cnt += 1
        T_groups[-1] = (cur, cnt)
    else:
        cnt = 1
        cur = c
        T_groups.append((cur, cnt))


if len(S_groups) != len(T_groups):
    print("No")
    exit()

for s, t in zip(S_groups, T_groups):
    sc, scnt = s
    tc, tcnt = t

    if sc != tc:
        can = False
        break

    if tcnt == scnt:
        continue

    if not tcnt > scnt >= 2:
        can = False
        break


print("Yes" if can else "No")

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

H, W = map(int, input().split())

rows = []

for i in range(H):
    row = list(map(int, input().split()))
    rows.append(row)

horizontal_sum = list(map(sum, rows))

vertical_sum = [0 for i in range(W)]

for row in rows:
    for i, num in enumerate(row):
        vertical_sum[i] += num

for i in range(H):
    for j in range(W):
        num = rows[i][j]
        print(horizontal_sum[i] + vertical_sum[j] - num, end=" ")
    print("")

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

N = int(input())

boards = [[-1 for j in range(N)] for i in range(N)]

max_low = N * math.ceil((N / 2))

base = [i for i in range(1, N+1)]

for i in range(N):
    b = base.copy()
    if i % 2 == 0:
        boards[i] = list(map(lambda num: i // 2 * N + num, b))
    else:
        boards[i] = list(
            map(lambda num: i // 2 * N + num + max_low, b))

for row in boards:
    for num in row:
        print(num, end=" ")
    print("")

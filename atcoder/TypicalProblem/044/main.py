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

step = 0

for i in range(Q):
    T, x, y = map(int, input().split())
    if T == 1:
        x = (x - 1 - step) % N
        y = (y - 1 - step) % N
        A[x], A[y] = A[y], A[x]
    elif T == 2:
        step += 1
    elif T == 3:
        print(A[(x - step - 1) % N])

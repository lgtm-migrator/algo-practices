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
# input = sys.stdin.readline
# 文字列を入力する場合
# input_str = input()[:-1]

INF = 2 << 60
MOD = 998244353

N, M, T = map(int, input().split())
A = list(map(int, input().split()))

bonus_list = defaultdict(int)

for i in range(M):
    x, y = map(int, input().split())
    bonus_list[x] = y

remain = T

can = False

# 一番目の部屋
remain += bonus_list[1]

for i in range(2, N+1):
    # i番目の部屋にいく
    remain -= A[i-2]
    if remain <= 0:
        can = False
        break
    remain += bonus_list[i]
    if remain > 0:
        can = True

print("Yes" if can else "No")

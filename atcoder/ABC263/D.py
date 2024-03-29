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

N, L, R = map(int, input().split())


A = list(map(int, input().split()))

ans = INF

for i in range(N+1):
    for j in range(N+1):
        tmp = sum(A[i:N - j]) + R * j + L * i
        ans = min(ans, tmp)

print(ans)

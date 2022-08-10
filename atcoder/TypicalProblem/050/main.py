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
MOD = 1_000_000_000 + 7

N, L = map(int, input().split())

dp = [0 for i in range(N+1)]
dp[0] = 1

for i in range(1, N+1):
    # 一つ前から来る場合
    dp[i] = dp[i-1]
    # Lつ前から来れる場合
    if i >= L:
        dp[i] += dp[i-L]
    dp[i] %= MOD

print(dp[N])

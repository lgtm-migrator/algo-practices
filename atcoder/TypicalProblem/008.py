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
MOD = 10 ** 9 + 7

N = int(input())
S = list(map(str, input()))

# dp[i][j]はi番目までの数字の中で"atcoder"のj番目の文字までが満たせる場合の数
dp = [[0 for j in range(8)] for i in range(N+1)]

char_map = {
    "a": 1,
    "t": 2,
    "c": 3,
    "o": 4,
    "d": 5,
    "e": 6,
    "r": 7,
}

for i in range(N+1):
    dp[i][0] = 1

for i in range(1, N+1):
    c = S[i-1]
    for j in range(1, 8):
        # 選ばない場合
        dp[i][j] = (dp[i][j] + dp[i-1][j]) % MOD
        if c in char_map.keys() and char_map[c] == j:
            # 選ぶ場合
            dp[i][j] = (dp[i][j] + dp[i-1][j-1]) % MOD

print(dp[N][7])

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

N, M = map(int, input().split())

# 桁数が単調増加
# 単調増加なので部分和問題としてdpが使える

# dp[i][j]...Aiがj桁の整数であり、Aの桁数が単調増加するような整数数列の個数
dp = [0 for i in range(60)] * 60
dp[0][0] = 1

for i in range(1, 60):
    for j in range(1, 60+1):
        # 選ばない場合
        dp[i][j] += dp[i-1][j]
        # 選ぶ場合

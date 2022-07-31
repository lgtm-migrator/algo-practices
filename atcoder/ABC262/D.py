from collections import defaultdict
from copy import copy
from typing import Generic, Iterable, Iterator, Set, Tuple, TypeVar, Union, List
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
A = list(map(int, input().split()))

ans = 0

sums = defaultdict(list)

dp = [[[0 for i in range(N+1)] for j in range(N+1)] for k in range(N+1)]

for n in range(1, N):
    for i in range(1, N+1):
        for j in range(1, N+1):
            s = sum(A[i:j+1])
            dp[i][j][s % (j-i+1)] += 1


for j in range(1, N+1):
    ans += dp[N][j][0]

print(ans)

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

N, X, Y = map(int, input().split())

memo = dict()
# blue
memo[0] = dict()
# red
memo[1] = dict()


def rec(level: int, is_red: bool) -> int:
    global X, Y, memo
    if memo[is_red].get(level) is not None:
        return memo[is_red][level]
    if level < 2:
        if level == 1 and not is_red:
            memo[is_red][level] = 1
            return 1
        else:
            return 0
    sum = 0
    if is_red:
        sum += rec(level - 1, True)
        for _ in range(X):
            sum += rec(level, False)
    else:
        sum += rec(level - 1, True)
        for _ in range(Y):
            sum += rec(level - 1, False)
    memo[is_red][level] = sum
    return sum


ans = rec(N, True)
print(ans)

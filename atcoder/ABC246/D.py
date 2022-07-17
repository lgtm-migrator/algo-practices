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


input = sys.stdin.readline

INF = 2 << 60
MOD = 998244353

N = int(input())


def calc(a: float, b: float) -> float:
    return (a + b) * (a ** 2 + b ** 2)


ans = 10 ** 18

for a in range(10**6+1):
    l = -1
    r = 10 ** 6
    while r - l != 1:
        mid = l + (r - l) // 2
        val = calc(a, mid)
        if val >= N:
            ans = min(ans, val)
            r = mid
        else:
            l = mid

print(ans)

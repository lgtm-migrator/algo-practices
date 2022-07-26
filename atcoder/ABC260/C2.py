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

reds = [0 for i in range(N+1)]
blues = [0 for i in range(N+1)]

reds[N] = 1

for i in reversed(range(2, N+1)):
    reds[i-1] += reds[i]
    blues[i] += X * reds[i]

    reds[i-1] += blues[i]
    blues[i-1] += Y * blues[i]

print(blues[1])

import datetime
import re
from bisect import bisect_left, bisect_right, insort_left, insort_right
import random
import heapq
from queue import PriorityQueue
from collections import Counter, defaultdict
import itertools
from collections import deque
import math
import decimal
import statistics
import sys

sys.setrecursionlimit(10**6)

INF = 2 << 60


N, a, b = map(int, input().split())

A = list(map(int, input().split()))

l = min(A)
r = max(A)


while r - l > 1:
    mid = l + (r - l) // 2
    xi = 0
    yi = 0
    for ai in A:
        if ai < mid:
            xi += math.ceil((mid - ai) / a)
        else:
            yi += (ai - mid) // b
    if xi <= yi:
        l = mid
    else:
        r = mid

print(l)

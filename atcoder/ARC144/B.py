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


input = sys.stdin.readline

INF = 2 << 60


N, a, b = map(int, input().split())

A = list(map(int, input().split()))
A.sort()

print("A", A)

lA = len(A)

cur_i = 0
cur_j = lA - 1

while cur_i < cur_j:
    print("cur_i", cur_i, "cur_j", cur_j)
    A[cur_i] += a
    A[cur_j] -= b
    if cur_i < lA - 1 and A[cur_i] > A[cur_i + 1]:
        A[cur_i] -= a
        cur_i += 1
    elif cur_j > 1 and A[cur_j] < A[cur_j - 1]:
        A[cur_j] -= b
        cur_j -= 1

print("A", A)
print(min(A))

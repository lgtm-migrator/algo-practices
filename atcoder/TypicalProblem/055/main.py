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

N, MOD, Q = map(int, input().split())

A = list(map(int, input().split()))

ans = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            for l in range(k+1, N):
                for m in range(l+1, N):
                    val = A[i] * A[j] % MOD * A[k] % MOD * \
                        A[l] % MOD * A[m] % MOD
                    if val == Q:
                        ans += 1

print(ans)

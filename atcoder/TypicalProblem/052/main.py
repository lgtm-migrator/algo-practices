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

N = int(input())
A = []

for i in range(N):
    a = list(map(int, input().split()))
    A.append(a)

ans = 1

for i in range(N):
    a_list = A[i]
    ans *= sum(a_list)
    ans %= MOD

print(ans)

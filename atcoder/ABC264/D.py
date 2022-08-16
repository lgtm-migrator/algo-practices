from cmath import cos
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
# input = sys.stdin.readline
# 文字列を入力する場合
# input_str = input()[:-1]

INF = 2 << 60
MOD = 998244353

S = list(map(str, input()))

origin = {
    "a": 0,
    "t": 1,
    "c": 2,
    "o": 3,
    "d": 4,
    "e": 5,
    "r": 6,
}

costs = []

start = None
ans = 0

tyokin = [0 for i in range(7)]

Origin = ["a", "t", "c", "o", "d", "e", "r"]
Origin.reverse()

i = 0

while Origin:
    c = S[i]
    if Origin[-1] == c:
        ans += i - origin[c] + tyokin[i]
        for j in range(i+1):
            tyokin[j] += 1
        Origin.pop()
    else:
        i += 1
        i %= 7

print(ans)

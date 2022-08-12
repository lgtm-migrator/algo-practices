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
MOD = 998244353

N = int(input())

X, Y = [], []
cost = 0


def getMedianX() -> float:
    X.sort()
    return X[len(X) // 2]


def getMedianY() -> float:
    Y.sort()
    return Y[len(Y) // 2]


for i in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

median_x, median_y = getMedianX(), getMedianY()

for x, y in zip(X, Y):
    if x == median_x and y == median_y:
        continue
    cost += abs(x - median_x) + abs(y - median_y)

print(int(cost))

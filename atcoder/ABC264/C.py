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

H1, W1 = map(int, input().split())

A = []

for i in range(H1):
    row = list(map(int, input().split()))
    A.append(row)

H2, W2 = map(int, input().split())

B = []

for i in range(H2):
    row = list(map(int, input().split()))
    B.append(row)


class Pos:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


for i, b in enumerate(B):
    cur = 0
    for j, b in enumerate(b):
        for k, a in enumerate(A):

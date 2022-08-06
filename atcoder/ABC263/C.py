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

N, M = map(int, input().split())

for a in range(1, M+1):
    if N == 1:
        print(a)
    for b in range(a+1, M+1):
        if N == 2:
            print(a, b)
        for c in range(b + 1, M+1):
            if N == 3:
                print(a, b, c)
            for d in range(c+1, M+1):
                if N == 4:
                    print(a, b, c, d)
                for e in range(d+1, M+1):
                    if N == 5:
                        print(a, b, c, d, e)
                    for f in range(e+1, M+1):
                        if N == 6:
                            print(a, b, c, d, e, f)
                        for g in range(f+1, M+1):
                            if N == 7:
                                print(a, b, c, d, e, f, g)
                            for h in range(g+1, M+1):
                                if N == 8:
                                    print(a, b, c, d, e, f, g, h)
                                for i in range(h+1, M+1):
                                    if N == 9:
                                        print(a, b, c, d, e, f, g, h, i)
                                    for j in range(i+1, M+1):
                                        if N == 10:
                                            print(a, b, c, d, e, f,
                                                  g, h, i, j)

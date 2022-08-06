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

P = list(map(int, input().split()))


def rec(index: int, cnt: int) -> int:
    if index >= 2 and index <= N:
        cnt += 1
        return rec(P[index - 2], cnt)
    return cnt


ans = rec(N, 0)
print(ans)

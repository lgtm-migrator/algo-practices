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

INF = 2 << 60
MOD = 998244353

N = int(input())

A = list(map(int, input().split()))

# key: index, val: int (対応するペアのindex)
cache = {}
sames = []

for i, num in enumerate(A):
    i += 1
    if i == num:
        sames.append(i)
    else:
        j = A[num-1]
        if i == j and i < num:
            cache[i] = num
            # print("add", "i:", i, "j:", j, "num:", num)

# print("sames", sames)
# print("cache", cache)

ans = 0

len_sames = len(sames)
ans += len_sames * (len_sames-1) // 2
ans += len(cache)

print(ans)

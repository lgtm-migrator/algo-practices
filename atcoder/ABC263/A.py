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

nums = list(map(int, input().split()))

kinds = dict()

for num in nums:
    if kinds.get(num) is None:
        kinds[num] = 0
    kinds[num] += 1


if len(kinds.keys()) != 2:
    print("No")
else:
    exp = {2, 3}
    for key in kinds.keys():
        if kinds[key] in exp:
            exp.remove(kinds[key])
    if len(exp) == 0:
        print("Yes")
    else:
        print("No")

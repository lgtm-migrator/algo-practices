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

S = list(map(str, input()))
kinds = set(S)
# print(kinds)
for kind in kinds:
    if S.count(kind) == 1:
        print(kind)
        exit()
print(-1)

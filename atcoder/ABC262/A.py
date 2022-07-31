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

Y = int(input())

pert = Y % 4
if pert == 0:
    pert = 2
elif pert == 2:
    pert = 0
ans = Y + pert
print(ans)

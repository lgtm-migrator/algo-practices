import datetime
from email.policy import default
import re
from bisect import bisect_left, bisect_right
import random
import heapq
from queue import PriorityQueue
from collections import Counter, defaultdict
import itertools
from collections import deque
import math
import decimal
import sys
from typing import Dict, List, Optional

sys.setrecursionlimit(10**6)

INF = 2 << 60
MOD = 998244353


N, K = map(int, input().split())
P = list(map(int, input().split()))

index_P = dict()
for i, p in enumerate(P):
    index_P[p] = i


class State:
    def __init__(self, on_field: List[int] = [], dups: Dict[int, List[int]] = {}):
        self.on_field = on_field
        self.dups = dups

    def __repr__(self) -> str:
        return f"{{ on_field: {self.on_field}, dups: {self.dups} }}"


state = State()

ans = [-1 for i in range(max(P))]

cur = 0
while cur < N:
    X = P[cur]
    index = cur
    print("X", X)
    if len(state.on_field) == 0 or max(list(map(lambda i: P[i], state.on_field))) < X:
        state.on_field.append(index)
        state.dups[cur] = [cur]
    else:
        l = -1
        bs_fields = state.on_field.copy()
        bs_fields = list(map(lambda i: P[i], state.on_field))
        bs_fields.sort()
        r = len(bs_fields)
        while r - l != 1:
            mid = l + (r - l) // 2
            mid_num = bs_fields[mid]
            if mid_num >= X:
                r = mid
            else:
                l = mid
        index = index_P[bs_fields[r]]
        print("cur", cur, "bs_index", index)
        assert index in state.on_field, "重ねようとしているのはfieldにない値です"

        state.dups[index].append(cur)
    if len(state.dups[index]) == K:
        for s in state.dups[index]:
            ans[P[s] - 1] = cur + 1
        state.on_field.remove(index)
        state.dups[index].clear()

    print("state", state)
    print("ans", ans)
    cur += 1

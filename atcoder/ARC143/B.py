import sys

# sys.setrecursionlimit(10**6)
# import decimal

import math
# from collections import deque
import itertools
# from collections import Counter
# from queue import PriorityQueue
# import heapq
# import decimal
# import random
# from bisect import bisect_left, bisect_right

# import re
# import datetime

input = sys.stdin.readline

INF = 2 << 60
MOD = 998244353


N = int(input())

# 条件を満たすものではなく、満たさないものから数えていく
# 全体の選び方
total = math.factorial(N**2) % MOD

# 条件を満たさないものの個数
cnt = 0
for i in range(2, N**2):
    pass

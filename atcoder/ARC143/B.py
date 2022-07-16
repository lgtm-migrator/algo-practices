import sys

# sys.setrecursionlimit(10**6)
# import decimal

# import math
# from collections import deque
# import itertools
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
total = math.factorial(N**2)

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


input = sys.stdin.readline

INF = 2 << 60

N = int(input())

head = N % 4
body = N // 4
num = str(4) * body
if head != 0:
    num = str(head) + num
x = int(num)
M = N * 2
print(M)
print(x)

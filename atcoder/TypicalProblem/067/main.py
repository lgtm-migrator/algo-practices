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

N, K = map(int, input().split())
N = str(N)


def convert8_to_10(nums: str) -> int:
    nums = list(map(str, nums))
    ans = 0
    i = 0
    while nums:
        num = int(nums.pop())
        ans = ans + (num) * 8 ** i
        i += 1
    return ans


def convert10_to_9(num: int) -> str:
    if num == 0:
        return "0"
    stack = deque()
    while num > 0:
        tmp = num % 9
        num //= 9
        stack.appendleft(str(tmp) if tmp != 8 else "5")
    return "".join(stack)


for i in range(K):
    tmp = convert8_to_10(N)
    # print(tmp)
    N = convert10_to_9(tmp)

print(int(N))

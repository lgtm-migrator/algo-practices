
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

phase = 1


class Applicant:
    def __init__(self, index: int, math_score: int, eng_score: int):
        self.index = index
        self.math_score = math_score
        self.eng_score = eng_score

    def __lt__(self, other):
        global phase
        if phase == 1:
            if self.math_score > other.math_score:
                return True
            elif self.math_score == other.math_score:
                return self.index < other.index
        elif phase == 2:
            if self.eng_score > other.eng_score:
                return True
            elif self.eng_score == other.eng_score:
                return self.index < other.index
        elif phase == 3:
            if self.eng_score + self.math_score > other.math_score + other.eng_score:
                return True
            elif self.eng_score + self.math_score == other.math_score + other.eng_score:
                return self.index < other.index
        return False

    def __repr__(self) -> str:
        return f"{{ index: {self.index}, math: {self.math_score} }}"


stack = []

N, X, Y, Z = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for i, (ai, bi) in enumerate(zip(A, B)):
    i += 1
    applicant = Applicant(i, ai, bi)
    stack.append(applicant)

ans = []


def sort1():
    global stack, phase
    phase = 1
    stack.sort(reverse=True)
    for _ in range(X):
        applicant = stack.pop()
        ans.append(applicant)


def sort2():
    global stack, phase
    phase = 2
    stack.sort(reverse=True)
    for _ in range(Y):
        applicant = stack.pop()
        ans.append(applicant)


def sort3():
    global stack, phase
    phase = 3
    stack.sort(reverse=True)
    for _ in range(Z):
        applicant = stack.pop()
        ans.append(applicant)


sort1()
sort2()
sort3()

ret = list(map(lambda a: a.index, ans))
ret.sort()
for num in ret:
    print(num)

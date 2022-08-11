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

H, W = map(int, input().split())

P = [[] for i in range(H)]

for i in range(H):
    row = list(map(int, input().split()))
    P[i] = row

ans = 0

for bit in range(1, 1 << H):
    # print("bit:", bin(bit))
    G = []
    # iは何桁目の数字を選ぶのかをチェックする
    # ex: 0b10101 ... 0, 2, 4番目の数字を選ぶ
    for w in range(W):
        # 縦で同じ数字が並んでいるかを確認する
        flag = False
        index = -1
        for h in range(H):
            if not (bit & (1 << h)):
                continue
            if index == -1:
                index = h
            elif P[index][w] != P[h][w]:
                flag = True
        if not flag:
            G.append(P[index][w])
    # Gからスコアを計算
    cnt_width = 0
    cnt_height = 0
    data = defaultdict(int)

    # print(G)

    for g in G:
        data[g] += 1
        cnt_width = max(cnt_width, data[g])

    for j in range(H):
        if (bit & (1 << j)) != 0:
            # 行を選ぶ場合
            cnt_height += 1

    # print(cnt_width, cnt_height)

    ans = max(ans, cnt_width * cnt_height)


print(ans)

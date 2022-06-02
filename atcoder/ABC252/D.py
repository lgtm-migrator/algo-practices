from collections import Counter
from itertools import combinations
import math

N = int(input())

nums = list(map(int, input().split()))


def nc3(n: int) -> int:
    return n * (n-1) * (n-2) // 2 // 3


def nc2(n: int) -> int:
    return n * (n - 1) // 2


counter = Counter(nums)

total = nc3(N)

for target in sorted(counter):
    cntx = counter[target]
    duplicate_twice = 0
    if cntx >= 2:
        duplicate_twice = (N - cntx) * nc2(cntx)
    duplicate_triple = 0
    if cntx >= 3:
        duplicate_triple = nc3(cntx)
    total -= duplicate_twice + duplicate_triple

print(int(total))

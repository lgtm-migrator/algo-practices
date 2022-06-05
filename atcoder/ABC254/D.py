from typing import List, Tuple
from collections import Counter

N = int(input())


def soinsu(x: int) -> List[int]:
    ret = []
    for i in range(2, x+1):
        if x % i == 0:
            ret.append(i)
            x /= i
        if x == 1:
            break
    return ret


for i in range(1, N+1):

from typing import List


def rec(n: int) -> List[int]:
    if n == 1:
        return [1]
    half = rec(n-1)
    return half + [n] + half


N = int(input())

all = rec(N)

for i, num in enumerate(all):
    print(num, end="\n" if i == len(all)-1 else " ")

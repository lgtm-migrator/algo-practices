from collections import deque
from concurrent.futures import thread
import math
from typing import List


N = int(input())

if N == 1:
    print(0)
    exit()


def Eratosthenes(x: int) -> List[int]:
    primes = []
    threshold = math.sqrt(x)
    removed = set()
    num = 2
    while True:
        if num in removed:
            num += 1
            continue
        for n in range(num*num, x+1, num):
            if n % num == 0:
                removed.add(n)
        if num >= threshold:
            break
        num += 1
    for num in range(2, x+1):
        if num not in removed:
            primes.append(num)
    return primes


candidates = Eratosthenes(10**6)

# print(candidates)

ans = 0

for i, p in enumerate(candidates[:-1]):
    l = i
    r = len(candidates)
    while r - l != 1:
        mid = l + (r - l) // 2
        q = candidates[mid]
        if p * (q ** 3) <= N:
            l = mid
        else:
            r = mid
    ans += l - i

print(ans)

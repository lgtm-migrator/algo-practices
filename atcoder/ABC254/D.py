import math
from typing import List, Tuple, Dict

N = int(input())


def prime_factorize(n: int) -> List[int]:
    a = dict()
    # 2を見つける
    while n % 2 == 0:
        if a.get(2) is None:
            a[2] = 1
        else:
            a[2] += 1
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            if a.get(f) is None:
                a[f] = 1
            else:
                a[f] += 1
            n //= f
        else:
            f += 2
    if n != 1:
        if a.get(n) is None:
            a[n] = 1
        else:
            a[n] += 1
    ans = []
    for num, cnt in a.items():
        if cnt % 2 == 0:
            continue
        ans.append(num)
    return ans


ans = 0


def get_number_of_squares() -> Dict[int, int]:
    s = dict()
    for i in range(1, N+1):
        j = 2
        s[i] = 1
        while j * j * i <= N:
            j += 1
            s[i] += 1
    return s


squares = get_number_of_squares()

for i in range(1, N+1):
    prime_fact = prime_factorize(i)
    fragment = 1
    for unique in prime_fact:
        fragment *= unique
    ans += squares[fragment]


print(ans)

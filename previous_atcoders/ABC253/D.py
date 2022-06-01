
import sys

sys.setrecursionlimit(10 ** 6)

N, A, B = map(int, input().split())

total = (1+N) * N // 2


def gcd(x: int, y: int) -> int:
    if x > y:
        if x % y == 0:
            return y
        else:
            return gcd(x % y, y)
    else:
        if y % x == 0:
            return x
        else:
            return gcd(x, y % x)


# a*b = LCM * GCD
def lcm(x: int, y: int) -> int:
    return x * y // gcd(x, y)


def sigma(x: int) -> int:
    return (x + 1) * x // 2


lcm_a_b = lcm(A, B)

cnt = N // A
total -= A * sigma(cnt)
cnt = N // B
total -= B * sigma(cnt)
cnt = N // lcm_a_b
if cnt > 0:
    total += lcm_a_b * sigma(cnt)

print(total)

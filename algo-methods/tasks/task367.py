N, M = map(int, input().split())


def f(x: float, years: float = 5) -> float:
    ret = N + 1
    for i in range(years):
        ret = ret * x + 1
    return ret


r = 100
l = 0.

while r - l > 10**-6:
    mid = (l + r) / 2
    if f(mid) > M:
        r = mid
    elif f(mid) < M:
        l = mid
    else:
        break

print(r)

import sys

N = int(input())

X = list(map(int, input().split()))


def f(x: int) -> int:
    return x * (x+1) // 2


ans = dict()

for x in X:
    if ans.get(x) is not None:
        print(ans[x])
        continue
    l = 0
    # 大きくとる
    r = 2 ** 60
    while r - l != 0:
        mid = (l + r) // 2
        s = f(mid)
        if s >= x:
            r = mid
        else:
            l = mid+1
    ans[x] = r
    print(r)

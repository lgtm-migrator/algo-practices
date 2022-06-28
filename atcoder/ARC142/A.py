N, K = map(int, input().split())


def f(x: int, prev: int) -> int:
    rev_x = int(str(x)[::-1])
    x = rev_x
    if prev == x or str(x)[::-1] == str(prev):
        return min(prev, x)
    return f(rev_x, x)


ans = []
if f(K, None) != K:
    print(0)
    exit(0)
# reverse
target = int(str(K)[::-1])
if K != target:
    while target <= N:
        ans.append(target)
        target *= 10
# normal
target = K
while target <= N:
    ans.append(target)
    target *= 10
# print(list(ans))
print(len(ans))

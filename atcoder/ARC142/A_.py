from itertools import permutations
import sys

sys.setrecursionlimit(10 ** 7)

N, K = map(int, input().split())

kinds = set()
kinds.add("0")
for k in str(K):
    kinds.add(k)


patterns = list(filter(lambda x: ((str(K) in "".join(x)) or ((str(K))[::-1] in "".join(x))) and int("".join(x)) <= N, list(
    permutations(kinds, len(kinds)))))

memo = dict()

m_k = min(K, int((str(K))[::-1]))


def f(o: int, x: int, prev: int) -> int:
    if memo.get(o) is not None:
        return memo[o]
    print(prev, x)
    if prev is not None:
        isSame = int(str(prev)) == int((str(x)[::-1]))
        if isSame:
            return min(prev, x)
    prev = x
    ans = f(o, int(str(x)[::-1]), prev)
    memo[o] = ans
    return ans


if N < K:
    print(0)
else:
    ans = 0
    for num in list(map(lambda x: int("".join(x)), patterns)):
        if K == f(num, num, None):
            ans += 1

    print(ans)

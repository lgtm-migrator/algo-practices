from typing import Set

N, M = map(int, input().split())

G = []

for i in range(N+1):
    G.append([])


for i in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

Q = int(input())


def sum_near_k(x: int, k: int, called: Set[int]) -> int:
    ret = 0
    if x not in called:
        ret += x
    called.add(x)
    if k == 0:
        return ret
    for n in G[x]:
        ret += sum_near_k(n, k-1, called)
    return ret


queries = []

for i in range(Q):
    x, k = map(int, input().split())
    queries.append((x, k))

for x, k in queries:
    print(sum_near_k(x, k, set()))

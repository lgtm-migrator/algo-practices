from itertools import combinations
from collections import Counter


N, K = map(int, input().split())

S_list = []

kinds = [chr(i) for i in range(ord("a"), ord("z") + 1)]

for i in range(N):
    S_list.append(input())

best = set()
for k in range(K, N+1):
    # k個選ぶ
    patterns = combinations(S_list, k)
    for pattern in patterns:
        ans = set()
        for target in kinds:
            count = 0
            for p in pattern:
                if target in p:
                    count += 1
            if count == K:
                ans.add(target)
        if len(ans) > len(best):
            best = ans

print(len(best))

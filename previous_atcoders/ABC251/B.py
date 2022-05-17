from itertools import combinations

N, W = map(int, input().split())
weights = sorted(list(map(int, input().split(" "))))

max_weight = min(W, sum(weights[-3:]))

ans = 0

possibles = set()

# 1個選ぶ
for v in list(filter(lambda w: w <= max_weight, weights)):
    possibles.add(v)

# 2個選ぶ
if len(weights) >= 2:
    comb = combinations(weights, 2)
    for v in comb:
        if sum(v) <= max_weight:
            possibles.add(sum(v))

# 3個選ぶ
if len(weights) >= 3:
    comb = combinations(weights, 3)
    for v in comb:
        if sum(v) <= max_weight:
            possibles.add(sum(v))

print(len(possibles))

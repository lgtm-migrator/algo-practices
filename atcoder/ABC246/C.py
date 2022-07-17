from bisect import insort
from collections import deque

N, K, X = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

capacity = 0

remains = []

for ai in A:
    capacity += ai // X
    remains.append(ai % X)

remains.sort(reverse=True)

total = sum(A)

used_coupon_cnt = min(capacity, K)

# print("remains", remains, "used_coupon_cnt", used_coupon_cnt)

total -= used_coupon_cnt * X
remain_coupon_cnt = K - used_coupon_cnt
subtract_from_remain_price = sum(remains[:remain_coupon_cnt])

total -= subtract_from_remain_price
print(total)

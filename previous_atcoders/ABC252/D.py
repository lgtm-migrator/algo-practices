from collections import Counter
from itertools import combinations

N = int(input())

nums = list(map(int, input().split()))

under_counter = {}
upper_counter = {}

for i, num in enumerate(nums):
    under = list(filter(lambda n: n != num, nums[:i]))
    upper = list(filter(lambda n: n != num and n not in under, nums[i:]))
    under_counter[num] = len(under)
    upper_counter[num] = len(upper)


print(under_counter)
print(upper_counter)
ans = 0

for j in range(2, N):
    # j = [2, N-1]
    num = nums[j]
    ans += under_counter[num] * upper_counter[num]

print(ans)

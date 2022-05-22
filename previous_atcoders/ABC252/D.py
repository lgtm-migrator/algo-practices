from collections import Counter

N = int(input())

nums = list(map(int, input().split()))

Counter(nums)

pairs = [(-1, -1, -1)]
for i, num in enumerate(nums):
    for j in range(i+1, N):
        if nums[i] == nums[j]:
            continue
        for k in range(j+1, N):
            if nums[j] == nums[k] or nums[k] == nums[i]:
                continue
            pairs.append((i, j, k))

print(len(list(set(pairs))) - 1)

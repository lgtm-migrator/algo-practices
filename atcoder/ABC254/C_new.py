from heapq import heappop, heappush

N, K = map(int, input().split())

nums = list(map(int, input().split()))

groups = []

for i in range(K):
    groups.append([])

# K-stepで配列の生成
# Kで割った余りが等しいindexを同じグループに入れる
for i in range(N + (K - N % K)):
    if len(nums) <= i:
        num = 2 ** 60
    else:
        num = nums[i]
    groups[i % K].append(num)

for i, nums in enumerate(groups):
    groups[i] = sorted(nums)

can = True

for nums in zip(*groups):
    nums = list(nums)
    exp = sorted(nums)
    if exp != nums:
        can = False
        break

print("Yes" if can else "No")

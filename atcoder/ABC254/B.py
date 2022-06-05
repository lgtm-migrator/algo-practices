from typing import List

N = int(input())

ans = []
ans.append([1])

print(1)

for i in range(1, N):
    nums = []
    for j in range(i+1):
        if j == 0 or i == j:
            nums.append(1)
        else:
            nums.append(ans[i-1][j-1] + ans[i-1][j])
    ans.append(nums)
    for num in nums:
        print(num, end=" ")
    print("")

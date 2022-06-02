nums = list(map(int, input().split()))
s = sorted(nums)

if nums[1] == s[1]:
    print("Yes")
else:
    print("No")

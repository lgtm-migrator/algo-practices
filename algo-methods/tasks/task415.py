N, X = map(int, input().split())
nums = [-1] + list(map(int, input().split()))

ans = 0
while X != 0:
    ans += 1
    X = nums[X]

print(ans)

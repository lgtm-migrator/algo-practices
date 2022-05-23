N = int(input())

nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

for i in range(N):
    inputs = list(map(int, input().split()))
    if len(inputs) == 3:
        nums[inputs[1]] = inputs[2]
    else:
        print(nums[inputs[1]])

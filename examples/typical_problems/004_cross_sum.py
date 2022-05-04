H, W = map(int, input().split())
nums = []
for i in range(H):
  row = list(map(int, input().split()))
  nums = nums + [row]
  
W_nums = [0] * W
H_nums = [0] * H

for h in range(H):    
  if H_nums[h] == 0:
    H_nums[h] = sum(nums[h][:])
  for w in range(W):
    if W_nums[w] == 0:
      W_nums[w] = sum(map(lambda x: x[w], nums))
    num = nums[h][w]
    col = W_nums[w]
    row = H_nums[h]
    print(col + row - num, end="\n" if w == W-1 else " ")

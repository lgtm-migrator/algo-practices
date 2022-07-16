N, K = map(int, input().split())

A = list(map(int, input().split()))

s = sum(A[:K])


class Num:
    def __init__(self, val: int, index: int):
        self.val = val
        self.index = index

    def __lt__(self, other):
        return self.index < other.index

    def __repr__(self) -> str:
        return f"{{val: {self.val}, index: {self.index}}}"


nums = []

for i, ai in enumerate(A):
    i += 1
    nums.append(Num(ai, i))


nums.sort()

# print(nums)

j = -1
aj = -1

best_cnt = -1

for num in nums:
    i = num.index
    print(num)
    if i <= K:
        # まだKの中
        if j <= i:
            j = i
            aj = num.val
    else:
        if aj >= num.val:
            continue
        # 入れ替えることでスコアが上昇すれば交換
        cnt = i - j
        if best_cnt == -1 or cnt < best_cnt:
            best_cnt = cnt

print(best_cnt)

N = int(input())


class ListNode:
    def __init__(self, start, end, next):
        self.start = start
        self.end = end
        self.next = next

    def print(self):
        print(self.start, self.end)


nums = []

for i in range(N):
    a, b = map(int, input().split())
    nums.append((a, b))

nums = list(set(nums))

nums.sort()

nil = ListNode(nums[0][0], nums[0][1], None)

origin = nil

cur = origin


for start, end in nums[1:]:
    # print("start", start, "end", end)
    new = ListNode(start, end, None)
    if cur.end >= new.start:
        cur.end = max(new.end, cur.end)
        if cur.end < new.end:
            cur.end = new.end
    else:
        cur.next = new
        cur = new

start = origin

while start != None:
    start.print()
    start = start.next

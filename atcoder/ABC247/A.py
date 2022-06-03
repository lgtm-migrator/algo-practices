class ListNode:
    def __init__(self, num: int, next=None):
        self.num = num
        self.next = next


nil = ListNode(-1)

S = list(map(int, input()))

for num in reversed(S):
    node = ListNode(num)
    node.next = nil.next
    nil.next = node

ret = [0]

cur: ListNode = nil.next
while cur.next is not None:
    node = cur
    cur = node.next
    ret.append(node.num)

print("".join(list(map(str, ret))))

from typing import Tuple, List
from queue import Queue, deque


class Balls:
    def __init__(self, cnt: int, num: int):
        self.cnt = cnt
        self.num = num


deq = deque()

Q = int(input())

inputs = []


for i in range(Q):
    inputs.append((list(map(int, input().split()))))

# 両端のデータのみを取り出したいときはdeque
for inp in inputs:
    if inp[0] == 1:
        x, c = inp[1], inp[2]
        new = Balls(c, x)
        deq.append(new)
    elif inp[0] == 2:
        c = inp[1]
        ball = deq[0]
        s = 0
        if c <= ball.cnt:
            s += ball.num * c
            deq[0].cnt -= c
            print(s)
            continue
        while c > 0:
            # print(f"ball: {ball.num}, {ball.cnt}")
            if c > ball.cnt:
                s += ball.num * ball.cnt
                c -= ball.cnt
                deq.popleft()
                ball = deq[0]
            else:
                s += ball.num * c
                deq[0].cnt -= c
                break
        print(s)

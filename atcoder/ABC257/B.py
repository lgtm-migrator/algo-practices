from typing import List
from collections import defaultdict

N, K, Q = map(int, input().split())


A_list = list(map(int, input().split()))

L_list = list(map(int, input().split()))


class Koma:
    def __init__(self, position: int):
        self.position = position


koma_list: List[Koma] = []

# key: position, dict: has_koma
field = defaultdict(lambda: 0)

for i in range(K):
    koma_list.append(Koma(A_list[i]))
    field[A_list[i]] = 1


def operate(li: int):
    target = koma_list[li-1]
    if target.position == N:
        return
    next_pos = target.position + 1
    if field.get(next_pos) is not None and field.get(next_pos) > 0:
        pass
    else:
        koma_list[li-1].position = next_pos
        field[next_pos] += 1
        field[next_pos-1] -= 1


for li in L_list:
    operate(li)


for koma in koma_list:
    print(koma.position, end=" ")

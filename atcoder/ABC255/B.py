from collections import defaultdict
import math
N, K = map(int, input().split())

light_nums = list(map(int, input().split()))


class Person:
    def __init__(self, num: int, x: float, y: float, has_light: bool):
        self.num = num
        self.x = x
        self.y = y
        self.has_light = has_light

    def distance(self, other):
        return math.sqrt(pow(abs(self.x - other.x), 2) + pow(abs(self.y - other.y), 2))


in_light_people = []
no_light_people = []


for i in range(1, N+1):
    has_light = i in light_nums
    x, y = map(float, input().split())
    p = Person(i, x, y, has_light)
    if has_light:
        in_light_people.append(p)
    else:
        no_light_people.append(p)


# 最小の距離リスト
memo = defaultdict(lambda: float(2 << 40))

for p in in_light_people:
    for target in no_light_people:
        distance = p.distance(target)
        memo[target.num] = min(memo[target.num], distance)

ans = max(memo.values())
print(ans)

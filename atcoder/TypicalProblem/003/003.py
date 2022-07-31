import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)


N = int(input())

G = []


class City:
    def __init__(self, num: int, cost: int = 1):
        self.num = num
        self.cost = cost

    def __str__(self):
        return f"{self.num}番目の都市"


cities = [City(i) for i in range(N)]

for i in range(N):
    G.append([])

for i in range(N-1):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    G[A].append(City(B))
    G[B].append(City(A))

# print([list(map(str, g)) for g in G])


def bfs(start: City):
    que = deque([start])
    seen = [False] * N
    seen[start.num] = True
    ret = [0] * N
    while len(que) > 0:
        city = que.popleft()
        for next in G[city.num]:
            if seen[next.num]:
                continue
            seen[next.num] = True
            ret[next.num] = ret[city.num] + next.cost
            que.append(next)
    longest, l = 0, []
    for i, num in enumerate(ret):
        if num == 0:
            continue
        if num > longest:
            l = [i]
            longest = num
        elif num == longest:
            l.append(i)
    return longest, l


ans = 0
# 末端を見つける。cityはなんでも良い
city = cities[0]
# print("city index:", city.num)
longest, city_indexes = bfs(city)
# print("city_indexes", city_indexes)
city_i = city_indexes[0]
l_city = City(city_i)
longest, _ = bfs(l_city)
# print("longest", longest)
ans = max(longest, ans)

print(ans+1)

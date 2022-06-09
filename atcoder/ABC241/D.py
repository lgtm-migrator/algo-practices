from heapq import heappop, heappush, heapify


G = []


def ope_1(x: int):
    heappush(G, x)


def ope_2(x: int, k: int):
    tmp_G = list(map(lambda num: num * -1, filter(lambda a: a <= x, G)))
    if len(tmp_G) == 0:
        print(-1)
        return
    heapify(tmp_G)
    called = set()
    best = heappop(tmp_G) * -1
    called.add(best)
    cnt = G.count(best)
    while cnt < k:
        if len(tmp_G) == 0:
            print(-1)
            return
        best = heappop(tmp_G) * -1
        if best in called:
            continue
        cnt += G.count(best)
        called.add(best)
    print(best)


def ope_3(x: int, k: int):
    tmp_G = list(filter(lambda a: a >= x, G))
    if len(tmp_G) == 0:
        print(-1)
        return
    heapify(tmp_G)
    called = set()
    best = heappop(tmp_G)
    called.add(best)
    cnt = G.count(best)
    while cnt < k:
        if len(tmp_G) == 0:
            print(-1)
            return
        best = heappop(tmp_G)
        if best in called:
            continue
        cnt += G.count(best)
        called.add(best)
    print(best)


Q = int(input())

commands = []

for i in range(Q):
    commands.append(list(map(int, input().split())))

for command in commands:
    if command[0] == 1:
        ope_1(command[1])
    elif command[0] == 2:
        x, k = command[1:]
        ope_2(x, k)
    elif command[0] == 3:
        x, k = command[1:]
        ope_3(x, k)

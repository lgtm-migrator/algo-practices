from heapq import heappop, heappush

S = dict()
max_h = []
min_h = []


def method1(x: int):
    S.setdefault(x, 0)
    S[x] += 1
    # priority queueは最大値を直接O(1)で見つけられない
    # -1をかけてheapifyすればO(1)で見つけられる
    heappush(max_h, -1 * x)
    heappush(min_h, x)


def method2(x: int, c: int):
    S.setdefault(x, 0)
    cnt = min(c, S[x])
    S[x] -= cnt


def method3():
    max_num = None
    while S[max_h[0]*(-1)] <= 0:
        heappop(max_h)

    while S[min_h[0]] <= 0:
        heappop(min_h)

    print(-max_h[0] - min_h[0])


Q = int(input())

for i in range(Q):
    inputs = list(map(int, input().split()))
    command = inputs[0]
    if command == 1:
        method1(inputs[1])
    elif command == 2:
        method2(inputs[1], inputs[2])
    elif command == 3:
        method3()

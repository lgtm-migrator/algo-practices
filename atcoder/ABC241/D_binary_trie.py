from heapq import heappop, heappush, heapify


G = []


def ope_1(x: int):
    pass


def ope_2(x: int, k: int):
    pass


def ope_3(x: int, k: int):
    pass


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

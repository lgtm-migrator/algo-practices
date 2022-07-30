from typing import List
import sys

sys.setrecursionlimit(10 ** 6)

H, W = map(int, input().split())


class Block:
    def __init__(self, val: str, x: int, y: int):
        self.val = val
        self.x = x
        self.y = y

    def can_enter(self) -> bool:
        return self.val in ["s", "g", "."]


fields: List[List[Block]] = [[None for i in range(W)] for j in range(H)]

dxs = [-1, 0, 0, 1]
dys = [0, 1, -1, 0]

start = None
goal = None

for i in range(H):
    blocks = list(map(str, input()))
    for j, c in enumerate(blocks):
        block = Block(c, j, i)
        if c == "s":
            start = block
        elif c == "g":
            goal = block
        fields[i][j] = block

seen = [[False for i in range(W)] for j in range(H)]

ans = False


def dfs(edge: Block):
    global ans
    seen[edge.y][edge.x] = True
    if ans:
        return

    if edge.val == "g":
        ans = True
        return

    for dx, dy in zip(dxs, dys):
        x = edge.x + dx
        y = edge.y + dy
        if x < 0 or x >= W:
            continue
        if y < 0 or y >= H:
            continue
        if seen[y][x]:
            continue
        nxt = fields[y][x]
        if not nxt.can_enter():
            continue
        dfs(nxt)


dfs(start)
print("Yes" if ans else "No")

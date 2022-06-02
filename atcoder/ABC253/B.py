from typing import List

H, W = map(int, input().split())

board = [[None] * W for i in range(H)]


class Position:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


def diff(self: Position, other: Position):
    return abs(self.x - other.x) + abs(self.y - other.y)


circles: List[Position] = []

for i in range(H):
    row = list(map(str, input()))
    board[i] = row
    for j, item in enumerate(row):
        if item == "o":
            circles.append(Position(j, i))

ans = diff(circles[0], circles[1])

print(ans)

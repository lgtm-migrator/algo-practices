N = int(input())


class JumpPlatform:
    def __init__(self, x: int, y: int, p: int):
        self.x = x
        self.y = y
        self.p = p

    def __eq__(self, o):
        return self.x == o.x and self.y == o.y


platforms = []

S = 0


def can_jump(train_cnt: int, f: JumpPlatform, d: JumpPlatform) -> bool:
    return train_cnt * f.p >= abs(f.x - d.x) + abs(f.y - d.y)


for i in range(N):
    x, y, P = map(int, input().split())
    platform = JumpPlatform(x, y, P)
    platforms.append(platform)

cnt = 0

# 1. 訓練回数を二分探索する
# 3. 出発点を全探索
# 4. 出発点からcan_jumpがTrueのものだけを選び、有向辺を貼る

l = 0
r = 2 * (10**9)


while r - l != 1:
    mid = l + (r - l) // 2
    for i in range(N):
        start = platforms[i]
        G = []
        for i in range(N):
            G.append([])
        for platform in platforms:
            if platform == start:
                continue
            if can_jump(mid, start, platform):
                G[i].append(platform)

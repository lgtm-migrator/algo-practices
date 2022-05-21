from queue import Queue

# 4方向への移動を表すベクトル
# (dxs, dys)で使用
# 0:下, 1:右, 2:上, 3:左
dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

H, W = map(int, input().split())
X0, Y0, X1, Y1 = map(int, input().split())

data = [[] for i in range(H)]

for i in range(H):
    S = list(map(str, input()))
    data[i] = S

dist = [[-1] * W for i in range(H)]
todo = Queue()

dist[X0][Y0] = 0
todo.put((X0, Y0))


while not todo.empty():
    startX, startY = todo.get()
    for dx, dy in zip(dxs, dys):
        # 隣接する点
        x = startX + dx
        y = startY + dy
        if x >= H or y >= W or x < 0 or y < 0:
            continue
        if data[x][y] == "B":
            continue
        if data[x][y] == "W":
            if dist[x][y] != -1:
                continue
            dist[x][y] = dist[startX][startY] + 1
            todo.put((x, y))

print(dist[X1][Y1])

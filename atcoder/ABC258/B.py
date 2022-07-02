

fields = []

N = int(input())

# (i, j) = (横, 縦)
max_list = []
max_num = 0

for i in range(1, N+1):
    row = list(map(int, input()))
    fields.append(row)
    for j, item in enumerate(row):
        j += 1
        if max_num == item:
            max_list.append((i, j))
        elif max_num < item:
            max_list = [(i, j)]
            max_num = item


def find_best_way(x: int, y: int, diff_x: int, diff_y: int):
    # (数字, 位置)
    bests = -1, -1
    neighbor_x, neighbor_y = x + diff_x, y + diff_y
    if neighbor_x < 1:
        neighbor_x = N
    elif neighbor_x > N:
        neighbor_x = 1
    if neighbor_y < 1:
        neighbor_y = N
    elif neighbor_y > N:
        neighbor_y = 1
    best = bests[0]
    val = fields[neighbor_x-1][neighbor_y-1]
    pos = neighbor_x, neighbor_y
    if best < val:
        bests = val, pos
    elif best == val:
        bests[1] = pos
    return bests


best_ans = -1

for diff_x, diff_y in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
    for x, y in max_list:
        ans = str(max_num)
        traces = [(x, y)]
        # N-1回移動する
        for i in range(N-1):
            x, y = traces[-1]
            nexts = find_best_way(x, y, diff_x, diff_y)
            # (数字, 位置)
            best, positions = nexts
            position_x, position_y = positions
            traces.append((position_x, position_y))
            # print(best, position_x, position_y)
            ans += str(best)
        best_ans = max(int(ans), best_ans)

print(best_ans)

N = int(input())

S = [[-1] * N for i in range(N)]

for i in range(N):
    S[i] = list(map(str, input()))

can = False

for i in range(N):
    if can:
        break
    for j in range(N):
        if can:
            break
        # 縦を見る
        if i + 5 < N:
            cnt = 0
            for k in range(6):
                if S[i+k][j] == "#":
                    cnt += 1
            if cnt >= 4:
                can = True
                break
        # 横を見る
        if j + 5 < N:
            cnt = 0
            for k in range(6):
                if S[i][j+k] == "#":
                    cnt += 1
            if cnt >= 4:
                can = True
                break
        if j + 5 < N and i + 5 < N:
            group = 0
            rev_group = 0
            for k in range(6):
                if S[i+k][j+k] == "#":
                    group += 1
                if S[i+k][j + 5 - k] == "#":
                    rev_group += 1
            if group >= 4 or rev_group >= 4:
                can = True
                break


print("Yes" if can else "No")

N = int(input())

S = [[-1] * N for i in range(N)]

for i in range(N):
    S[i] = list(map(str, input()))

can = False

for i in range(N-6+1):
    if can:
        break
    max_i = i + 5
    is_last_i = max_i == N - 1
    if max_i >= N:
        continue
    for j in range(N-6+1):
        if can:
            break
        max_j = j + 5
        is_last_j = j == N-1
        if max_j >= N:
            continue
        values = S[j:max_j+1][i:max_i+1]
        # 縦を探す
        if is_last_i:
            for k in range(6):
                if values[:][k].count("#") >= 4:
                    can = True
                    break
        else:
            if values[:][0].count("#") >= 4:
                can = True
                break

        # 横を探す
        if is_last_j:
            for k in range(6):
                if values[k][:].count("#") >= 4:
                    can = True
                    break
        else:
            if values[0][:].count("#") >= 4:
                can = True
                break

        # 斜を探す
        nums = []
        for k in range(6):
            nums.append(values[k][k])
        if nums.count("#") >= 4:
            can = True
            break


print("Yes" if can else "No")

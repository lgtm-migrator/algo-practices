N, A, B = map(int, input().split())

tile = [[""] * B for i in range(A)]

tiles = [[""] * N for i in range(N)]

tiles[0][0] = "."

for h, row in enumerate(tiles):
    for w, t in enumerate(row):
        if t == "":
            ws = [w - 1, w]
            hs = [h - 1, h]
            for nh in hs:
                for nw in ws:
                    if abs(nw - w) + abs(nh - h) != 1:
                        continue
                        print(f"nw: {nw}, nh: {nh}")
                    if tiles[nh][nw] == ".":
                        tiles[h][w] = "#"
                    elif tiles[nh][nw] == "#":
                        tiles[h][w] = "."

for i in range(N):
    for _ in range(A):
        for j in range(N):
            row = tiles[i]
            s = ""
            s = s.join([row[j]] * B)
            print(s, end="")
        print("")

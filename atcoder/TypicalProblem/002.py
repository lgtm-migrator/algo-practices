N = int(input())

for i in range(2 ** N):
    s = ""
    for j in reversed(range(N)):
        if (i & (1 << j)) == 0:
            s += "("
        else:
            s += ")"
    open_cnt = 0
    close_cnt = 0
    ok = True
    for c in s:
        if c == ")":
            close_cnt += 1
        else:
            open_cnt += 1
        if open_cnt < close_cnt:
            ok = False
            break
    if ok:
        if open_cnt == close_cnt:
            print(s)

from collections import deque
N = int(input())
S = list(map(str, input()))

i = 1

W_list = [0]

for c in S:
    if c == "A":
        W_list[-1] += 2
    elif c == "B":
        W_list[-1] += 1
    else:
        W_list.append(0)

ans = ""
w = W_list[0]
if w % 2 == 0:
    ans += "".join(["A"] * (w // 2))
else:
    ans += "".join(["A"] * ((w - 1) // 2)) + "B"

for w in W_list[1:]:
    ans += "C"
    if w % 2 == 0:
        ans += "".join(["A"] * (w // 2))
    else:
        ans += "".join(["A"] * ((w - 1) // 2)) + "B"

print(ans)

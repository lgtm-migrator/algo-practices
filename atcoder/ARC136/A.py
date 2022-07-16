N = int(input())
S = list(map(str, input()))

ans = []
weight = 0

# 文字列は単に繋げるのではなく、配列で集めてから`"".join`した方が速い
for c in S:
    if c == "C":
        if weight % 2 == 0:
            a_num = weight // 2
            b_num = 0
        else:
            a_num = (weight - 1) // 2
            b_num = 1
        ans += ["A"] * a_num
        ans += ["B"] * b_num
        ans += ["C"]
        weight = 0
    else:
        weight += 2 if c == "A" else 1

if weight != 0:
    if weight % 2 == 0:
        a_num = weight // 2
        b_num = 0
    else:
        a_num = (weight - 1) // 2
        b_num = 1
    ans += ["A"] * a_num
    ans += ["B"] * b_num

print("".join(ans))

N = int(input())
S = input()

ret = 0
s = 1
count = len(S.split("ARC"))
S.replace("ARC", "AC", count//2)
ret += count//2
S.replace("ARC", "R", count//2)
ret += count//2

while True:
    can = -1
    for i in range(s, len(S)-1):
        arc = S[i-1] + S[i] + S[i+1]
        if arc == "ARC":
            can = i
            break
    if can == -1:
        break
    ret += 1
    if ret % 2 == 0:
        S = S.replace("ARC", "AC", 1)
        s = can + 2
    else:
        S = S.replace("ARC", "R", 1)
        s = can - 1


print(ret)

from collections import Counter

N = int(input())
inf = 100000
S = []
for i in range(N):
    s = list(map(int, map(str, input())))
    S.append(s)

ans = inf

for i in range(N):
    for k in range(10):
        correct = S[i][k]
        candidates = list(range(N))
        candidates.remove(i)
        times = [k]
        for candidate in candidates:
            for j, s in enumerate(S[candidate]):
                if s == correct:
                    times.append(j)
        dic = {}
        for t in times:
            if dic.get(t) is None:
                dic[t] = 0
            else:
                dic[t] += 1
        counter = Counter(dic)
        num = -1
        count = 0
        for n, c in counter.items():
            if c > count:
                count = c
                num = n
            elif c == count and num < n:
                num = n
        penalty = count * 10
        score = num + penalty
        if score < ans:
            ans = score

print(ans)

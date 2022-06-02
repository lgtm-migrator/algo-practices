N, K = map(int, input().split())
S = input()

divs = []
i = 1
while i*i <= N:
    if N % i == 0:
        divs.append(i)
        divs.append(N//i)
    i += 1

best = 2 ** 60
for div in sorted(list(set(divs))):
    characters = {d: [] for d in range(div)}
    for i, c in enumerate(S):
        characters[i % div].append(c)
    count = 0
    for index, chars in characters.items():
        m = max(map(lambda c: chars.count(c), set(chars)))
        count += N//div - m
    if count <= K:
        best = min(best, div)

print(best)

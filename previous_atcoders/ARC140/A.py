N, K = map(int, input().split())
S = input()

divs = []
for i in reversed(range(1, N+1)):
    if N % i == 0:
        divs.append(i)

best = 2 ** 60
for div in divs:
    characters = {d: [] for d in div}
    for i, c in enumerate(S):
        characters[i % div].append(c)
    count = 2 ** 60
    for index, chars in characters.items() {
        count += len(set(chars))
    }

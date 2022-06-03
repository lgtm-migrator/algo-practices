from collections import Counter

N = int(input())

names = dict()

for i in range(N):
    last, first = map(str, input().split())
    names[i] = [last, first]

can = True

for i in range(N):
    last, first = names[i]
    others = list(names.values())
    others.remove([last, first])
    others = sum(others, [])
    if last in others and first in others:
        can = False

print("Yes" if can else "No")


class Person(object):
    def __init__(self, weight: int, is_adult: bool):
        self.weight = weight
        self.is_adult = is_adult

    def __lt__(self, nxt):
        return self.weight < nxt.weight

    def __repr__(self):
        return str(self.weight)


people = []

N = int(input())

S = list(map(int, input()))

weights = list(map(int, input().split()))

# print(S)

num_adults = 0

for i, s in enumerate(S):
    weight = weights[i]
    if s == 0:
        people.append(Person(weight, False))
    else:
        people.append(Person(weight, True))
        num_adults += 1


people.sort()

# print(people)

best = num_adults
tmp = num_adults

# print(num_adults)

for i in range(N):
    if people[i].is_adult:
        tmp -= 1
    else:
        tmp += 1
    if i != N-1 and people[i].weight == people[i+1].weight:
        continue
    best = max(tmp, best)

print(best)

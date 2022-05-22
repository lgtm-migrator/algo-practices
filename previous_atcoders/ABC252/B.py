N, K = map(int, input().split())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))


best = [(0, -1)]
for i, a in enumerate(A_list):
    m = max(map(lambda x: x[1], best))
    if a > m:
        best = [(i+1, a)]
    elif a == m:
        best.append((i+1, a))

indexes = list(map(lambda x: x[0], best))

possible = False
for index in list(indexes):
    if index in B_list:
        possible = True
        break

if possible:
    print("Yes")
else:
    print("No")

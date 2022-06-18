from collections import deque
N, M = map(int, input().split())

G = []

for i in range(N):
    G.append([])

for i in range(M):
    f, s = map(int, input().split())
    G[f].append(s)


dependencies = [-1] * N

for task in range(N):
    dependencies[task] = len(G[task])

que = deque([])

# フリーになった点の個数
num = 0

for i, val in enumerate(dependencies):
    if val == 0:
        que.append(i)
        num += 1

print(que)

while len(que) > 0:
    cur = que.popleft()
    for next in G[cur]:
        dependencies[next] -= 1
        if dependencies[next] == 0:
            que.append(next)
            num += 1

print(dependencies)
print(num)

if num == N:
    print("Yes")
else:
    print("No")

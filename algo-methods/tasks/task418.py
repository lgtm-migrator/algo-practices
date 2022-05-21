from queue import Queue

N, M = map(int, input().split())

graph = [[] for i in range(N)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)


dist = [-1] * N
todo = Queue()

todo.put(0)
dist[0] = 0

while not todo.empty():
    start = todo.get()
    for vertex in graph[start]:
        if dist[vertex] == -1:
            dist[vertex] = dist[start] + 1
            todo.put(vertex)

print(max(dist))

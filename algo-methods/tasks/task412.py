N, M = map(int, input().split(" "))
turtles = [[] for i in range(N)]
for i in range(M):
    A, B = map(int, input().split(" "))
    turtles[A].append(B)

for i, turtle in enumerate(turtles):    
    for follow in sorted(turtle):
        print(follow, end=" ")
    if i < len(turtles) - 1:
        print("", end="\n")
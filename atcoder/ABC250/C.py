N, Q = map(int, input().split())

x_list = []
indexes = [-1] * 10**6

for i in range(1, N+1):
    x_list.append(i)
    indexes[i] = i-1

replaces = []

for i in range(Q):
    replaces.append(int(input()))

for replace in replaces:
    i = indexes[replace]
    if replace == x_list[i]:
        target = -1
        if i == N - 1:
            target = i-1
        else:
            target = i+1
        temp = x_list[target]
        x_list[target], x_list[i] = replace, temp
        indexes[temp], indexes[replace] = i, target


for i in range(N):
    print(x_list[i], end="\n" if i == len(x_list)-1 else " ")

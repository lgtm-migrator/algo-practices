R, C = map(int, input().split())

top = list(map(int, input().split()))
bottom = list(map(int, input().split()))

if R == 1:
    print(top[C-1])
else:
    print(bottom[C-1])

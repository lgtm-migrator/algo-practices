N = int(input())

weights = list(map(int, input().split()))

sorted_weights = sorted(weights)

for i in range(len(weights)):
    weight = weights[i]
    l = 0
    r = N
    while r - l != 0:
        mid = (l + r) // 2
        if weight == sorted_weights[mid]:
            l = mid
            break
        elif weight < sorted_weights[mid]:
            r = mid
        else:
            l = mid+1
    print(l)

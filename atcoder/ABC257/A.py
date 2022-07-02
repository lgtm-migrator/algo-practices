N, X = map(int, input().split())

index = X // N - 1
if X % N != 0:
    index += 1
print(chr(index + ord("A")))

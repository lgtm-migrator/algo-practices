import math


A, B = map(int, input().split())

distance = math.sqrt(A**2 + B ** 2)
x = A / distance
y = B / distance
print(x, y)

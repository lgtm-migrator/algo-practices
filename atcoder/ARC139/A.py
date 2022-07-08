from math import gcd


N = int(input())
T_list = list(map(int, input().split()))

last = 0

for t in T_list:
    num = 1 << t
    y_1 = ((last // num) + 1) * num
    y_2 = y_1 + num
    nxt = 1 << (t + 1)
    if y_1 % nxt != 0:
        last = y_1
    elif y_2 % nxt != 0:
        last = y_2

print(last)

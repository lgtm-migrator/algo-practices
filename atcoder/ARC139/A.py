import sys


N = int(input())
T_list = list(map(int, input().split()))

before = 0
before_digit = 1

A_list = []

for t in T_list:
    num = 1 << t
    while num <= before:
        if before_digit == t:
            num += 1 << (before_digit + 1)
        elif before_digit > t:
            num += 1 << before_digit
        else:
            num += 1 << (t + 1)
    # print("before", format(before, "b"))
    A_list.append(num)
    # print("num", format(num, "b"))
    before = num
    before_digit = t

print(A_list[-1])

import typing
import sys
sys.setrecursionlimit(10**6)


nums: typing.List[int] = []

memo: typing.List[typing.List[bool]] = []


def f(i: int, j: int) -> bool:
    if memo[i][j] is not None:
        return memo[i][j]
    if i == 0:
        memo[i][j] = j == 0
        return j == 0
    flag = False
    num = nums[i]
    if j - num >= 0 and f(i-1, j - num):
        flag = True
    if f(i-1, j):
        flag = True
    memo[i][j] = flag
    return flag


if __name__ == "__main__":
    N, X = map(int, input().split())
    nums = [0] + list(map(int, input().split()))
    memo = [[None] * (X+1) for i in range(N+1)]
    if f(N, X):
        print("Yes")
    else:
        print("No")

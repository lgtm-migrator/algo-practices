N, Q = map(int, input().split())

nums = list(map(int, input().split()))

memo = dict()


def calc_sum(i: int) -> int:

    for j in range(i):
        calc_sum(j)


def cmd1(x: int, v: int):
    nums[x] = v


def cmd2(x: int):
    pass

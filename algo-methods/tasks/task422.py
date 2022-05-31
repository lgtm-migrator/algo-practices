# スタックオーバーフローを防ぐ
import sys
sys.setrecursionlimit(10**6)

N = int(input())


def s(num: int) -> int:
    if num == 0:
        return 0
    return s(num - 1) + num


print(s(N))

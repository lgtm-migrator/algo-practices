# スタックオーバーフローを防ぐ
import sys
sys.setrecursionlimit(10**6)

A, B = map(int, input().split())


def sum(n: int, minimum: int) -> int:
    if minimum == n:
        return minimum
    return sum(n-1, minimum) + n


print(sum(B, A))

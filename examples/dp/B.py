from typing import List


def logic_B(N: int, K: int, costs: List[int]):
    dp: List[int] = [1e+7 for i in range(N)]

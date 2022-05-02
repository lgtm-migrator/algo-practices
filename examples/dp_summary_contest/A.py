from typing import List


def logic(n: int, costs: List[int]) -> int:
    dp: List[int] = list(map(lambda e: 1e+7, range(1, n+1)))
    dp[0] = 0
    for i in range(1, n):
        if i == 1:
            dp[i] = dp[0] + abs(costs[1] - costs[0])
        else:
            dp[i] = min(dp[i-1] + abs(costs[i]-costs[i-1]),
                        dp[i-2] + abs(costs[i]-costs[i-2]))
    return dp[n-1]


if __name__ == "__main__":
    N = int(input())
    h_list: List[int] = list(map(int, input().split()))
    print(logic(N, h_list))

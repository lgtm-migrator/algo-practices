from typing import List


def logic_B(N: int, K: int, costs: List[int]) -> int:
    dp: List[int] = [1e+7 for i in range(N)]
    dp[0] = 0
    for i in range(N-1):        
        if K == 1:
            dp[i+1] = min(dp[i] + abs(costs[i] - costs[i+1]), dp[i+1])
        else:
            for j in range(i+1, min(N, i+K+1)):
                dp[j] = min(dp[i] + abs(costs[i] - costs[j]), dp[j])
    return dp[N-1]


if __name__ == "__main__":
    N, K = map(int, input().split())
    costs = list(map(int, input().split()))
    ret = logic_B(N, K, costs)
    print(ret)
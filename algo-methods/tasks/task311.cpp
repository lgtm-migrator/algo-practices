#include <iostream>
#include <vector>

using namespace std;

const long long inf = 1LL << 20;

int main()
{
    long long N, M;
    cin >> N >> M;
    vector<long long> nums(N);
    for (long long i = 0; i < N; i++)
    {
        cin >> nums[i];
    }
    // dp[i+1][m] = <the minimum size to adjust sum of nums picked within i_th integers.>
    vector<vector<long long>> dp(N + 1, vector<long long>(M + 1, inf));
    dp[0][0] = 0;
    for (int i = 0; i < N; i++)
    {
        // decide whether I pick nums[i] or not.
        for (long long m = 0; m <= M; m++)
        {
            long long exp_cap = m - nums[i];
            // first, I assume that it is not possible to pick nums[i] due to weights limitation.
            dp[i + 1][m] = min(dp[i + 1][m], dp[i][m]);
            if (exp_cap >= 0)
            {
                // we can pick nums[i] in certain weight `m`.
                dp[i + 1][m] = min(dp[i][exp_cap] + 1, dp[i + 1][m]);
            }
        }
    }
    if (dp[N][M] == inf)
    {
        dp[N][M] = -1;
    }
    cout << dp[N][M] << endl;
    return 0;
}
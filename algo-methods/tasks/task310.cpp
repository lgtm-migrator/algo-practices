#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int N, M;
    cin >> N >> M;
    vector<int> nums(N);
    for (int i = 0; i < N; i++)
    {
        cin >> nums[i];
    }
    vector<vector<int>> dp(N + 1, vector(M + 1, 0));
    dp[0][0] = 1;
    for (int i = 1; i <= N; i++)
    {
        for (int m = 0; m <= M; m++)
        {
            if (m - nums[i - 1] >= 0)
            {
                dp[i][m] = dp[i - 1][m - nums[i - 1]] + dp[i - 1][m];
            }
            else
            {
                dp[i][m] = dp[i - 1][m];
            }
            dp[i][m] %= 1000;
        }
    }
    cout << dp[N][M] << endl;
    return 0;
}
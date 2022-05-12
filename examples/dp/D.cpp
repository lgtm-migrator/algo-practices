#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int N, W;
    cin >> N >> W;
    vector<int> weights(N + 1, 0);
    vector<int> values(N + 1, 0);
    for (int i = 1; i <= N; i++)
    {
        cin >> weights[i] >> values[i];
    }
    // もらう遷移
    vector<vector<long long>> dp(N + 1, vector<long long>(W + 1, 0));
    for (int i = 1; i <= N; i++)
    {
        for (int w = 1; w <= W; w++)
        {
            int capacity = w - weights[i];
            if (capacity >= 0)
            {
                dp[i][w] = max(dp[i - 1][capacity] + values[i], dp[i - 1][w]);
            }
            else
            {
                dp[i][w] = dp[i - 1][w];
            }
        }
    }
    cout << dp[N][W] << endl;
    return 0;
}
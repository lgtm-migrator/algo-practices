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
    // i番目の整数の中からいくつかの整数を選んで総和をjにできるかどうか
    // dp[i+1][j] = false/true;
    vector<vector<bool>> dp(N + 1, vector<bool>(M + 1, false));
    dp[0][0] = true;
    for (int i = 0; i < N; i++)
    {
        // Aiより前の数字は既に計算されているとして、Aiを選ぶかどうかだけを考える
        for (int j = 0; j <= M; j++)
        {
            if (j - nums[i] >= 0 && dp[i][j - nums[i]])
            {
                // 選ぶ場合
                dp[i + 1][j] = dp[i][j - nums[i]];
            }
            else
            {
                // 選ばない場合
                dp[i + 1][j] = dp[i][j];
            }
        }
    }
    if (dp[N][M])
    {
        cout << "Yes" << endl;
    }
    else
    {
        cout << "No" << endl;
    }
    return 0;
}
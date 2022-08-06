#include <iostream>
#include <vector>

using namespace std;

// 1LL << 20だと小さすぎる
// 1LL << 20は1048576
const long long inf = 1LL << 60;

template <class T, class V>
void format2(T &a, V &b, string label1, string label2, string head = "")
{
    cout << head << endl;
    cout << label1 << ": " << a << ", " << label2 << ": " << b << endl;
}

template <class T>
void format1(T &a, string label)
{
    cout << label << ": " << a << endl;
}

int main()
{
    // 重みが10^9まであるので価値を添字にする
    int N;
    long long W;
    cin >> N >> W;
    vector<long long> weights(100 + N);
    vector<long long> values(100 + N);
    for (int i = 1; i <= N; i++)
    {
        cin >> weights[i] >> values[i];
    }
    int V = 100100;
    // ありえない遷移については最大の重みコストを付与
    vector<vector<long long>> dp(N + 100, vector<long long>(V + 100, inf));
    dp[0][0] = 0;
    for (int i = 1; i <= N; i++)
    {
        for (int v = 0; v <= V + 100; v++)
        {
            if (v >= values[i])
            {
                dp[i][v] = min(dp[i - 1][v - values[i]] + weights[i], dp[i - 1][v]);
            }
            else
            {
                dp[i][v] = dp[i - 1][v];
            }
        }
    }
    int ans = 0;
    for (int v = 0; v <= V; v++)
    {
        if (dp[N][v] <= W)
        {
            ans = max(ans, v);
        }
    }
    cout << ans << endl;
    return 0;
}
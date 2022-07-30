#include <atcoder/all>
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>

using namespace atcoder;
using namespace std;
using ll = long long;

const ll INF = 1LL << 60;

int main()
{
    int N, M;
    cin >> N >> M;
    vector<ll> X;
    for (int i = 0; i < N; i++)
    {
        ll xi;
        cin >> xi;
        X.push_back(xi);
    }

    map<int, ll> B = {};

    for (int i = 0; i < M; i++)
    {
        ll ci;
        ll yi;
        cin >> ci >> yi;
        B[ci] = yi;
    }

    vector<vector<ll>> dp(N + 1, vector<ll>(N + 1, -INF));
    dp[0][0] = 0;
    ll prev_max = -INF;
    for (ll i = 1; i <= N; i++)
    {
        // 選ばない場合
        dp[i][0] = prev_max;
        for (ll j = 1; j <= i; j++)
        {
            // 選ぶ場合
            dp[i][j] = dp[i - 1][j - 1] + X[i - 1];
            if (B.count(j) != 0)
            {
                dp[i][j] += B[j];
            }
            prev_max = max(prev_max, dp[i][j]);
        }
    }
    ll ans = 0;
    for (int i = 1; i <= N; i++)
    {
        ans = max(dp[N][i], ans);
    }
    cout << ans;

    return 0;
}
#include <atcoder/all>
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>

using namespace atcoder;
using namespace std;
using ll = long long;
using mint = static_modint<1000000000 + 7>;

// 桁は最大でも100000桁
int main()
{
    ll K;
    cin >> K;
    // dp[i]...総和がiになり得る個数
    vector<mint> dp(100000LL, 0);
    dp[0] = 1;
    if (K % 9 != 0)
    {
        cout << 0 << endl;
        return 0;
    }
    for (ll i = 1; i <= 100000LL; i++)
    {
        for (int j = 1; j <= 9; j++)
        {
            if (i - j < 0)
            {
                continue;
            }
            dp[i] += dp[i - j];
        }
    }
    cout << dp[K].val() << endl;
    return 0;
}

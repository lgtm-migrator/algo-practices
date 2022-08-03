#include <atcoder/all>
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>

using namespace atcoder;
using namespace std;
using ll = long long;

int main()
{
    // いもす
    ll N;
    cin >> N;
    vector<vector<ll>> results(1100, vector<ll>(1100, 0));
    for (ll i = 0; i < N; i++)
    {
        ll lx, ly, rx, ry;
        cin >> lx >> ly >> rx >> ry;
        results[lx][ly] += 1;
        results[lx][ry] -= 1;
        results[rx][ly] -= 1;
        results[rx][ry] += 1;
    }
    for (ll i = 0; i <= 1000; i++)
    {
        for (ll j = 1; j <= 1000; j++)
        {
            results[i][j] += results[i][j - 1];
        }
    }
    for (ll i = 1; i <= 1000; i++)
    {
        for (ll j = 0; j <= 1000; j++)
        {
            results[i][j] += results[i - 1][j];
        }
    }
    vector<ll> ans(N + 1, 0);
    for (auto row : results)
    {
        for (auto result : row)
        {
            ans[result] += 1;
        }
    }
    for (ll i = 1; i <= N; i++)
    {
        cout << ans[i] << endl;
    }
    return 0;
}

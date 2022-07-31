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
    ll N, A, B, C;
    cin >> N;
    cin >> A >> B >> C;
    ll L = 9999;
    ll ans = 10000;
    for (ll i = 0; i <= L; i++)
    {
        for (ll j = 0; i + j <= L; j++)
        {
            ll remain = (N - (i * A) - (j * B));
            if (remain >= 0 && remain % C == 0)
            {
                ll k = remain / C;
                ans = min(ans, i + j + k);
            }
        }
    }
    cout << ans << endl;
    return 0;
}

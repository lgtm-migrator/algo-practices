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
    ll N;
    cin >> N;
    vector<ll> buttons(N);
    bool can = false;
    for (ll i = 0; i < N; i++)
    {
        cin >> buttons[i];
        if (buttons[i] == 2)
        {
            can = true;
        }
    }
    if (!can)
    {
        cout << -1 << endl;
        return 0;
    }
    ll cur = 1;
    ll cnt = 0;
    vector<bool> seen(N, false);
    while (true)
    {
        seen[cur - 1] = true;
        cnt += 1;
        if (buttons[cur - 1] == 2)
        {
            cout << cnt << endl;
            return 0;
        }
        if (cur == buttons[cur - 1] || seen[buttons[cur - 1] - 1])
        {
            cout << -1 << endl;
            return 0;
        }
        cur = buttons[cur - 1];
    }
    return 0;
}

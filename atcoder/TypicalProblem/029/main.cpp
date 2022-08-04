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
    ll W, N;
    cin >> W >> N;
    vector<ll> L(N);
    vector<ll> R(N);
    vector<ll> heights(W + 1, 0);
    for (ll i = 0; i < N; i++)
    {
        cin >> L[i] >> R[i];
    }
    for (ll i = 0; i < N; i++)
    {
        ll l = L[i];
        ll r = R[i];
        ll max_height = 0;
        for (ll j = l; j <= r; j++)
        {
            max_height = max(max_height, heights[j]);
        }
        for (ll j = l; j <= r; j++)
        {
            heights[j] = max_height + 1;
        }
        cout << max_height + 1 << endl;
    }

    return 0;
}

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
    ll ans = 0;
    vector<ll> A;
    vector<ll> B;
    for (ll i = 0; i < N; i++)
    {
        ll ai;
        cin >> ai;
        A.push_back(ai);
    }
    for (ll i = 0; i < N; i++)
    {
        ll bi;
        cin >> bi;
        B.push_back(bi);
    }
    sort(A.begin(), A.end());
    sort(B.begin(), B.end());
    for (ll i = 0; i < N; i++)
    {
        ans += abs(A[i] - B[i]);
    }
    cout << ans << endl;
    return 0;
}

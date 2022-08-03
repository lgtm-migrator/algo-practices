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
    ll N, K;
    cin >> N >> K;
    vector<ll> A(N), B(N);
    for (ll i = 0; i < N; i++)
    {
        cin >> A[i];
    }
    for (ll i = 0; i < N; i++)
    {
        cin >> B[i];
    }
    ll cnt = 0;
    for (ll i = 0; i < N; i++)
    {
        ll a = A[i];
        ll b = B[i];
        cnt += abs(a - b);
    }
    if (cnt <= K && abs(cnt - K) % 2 == 0)
    {
        cout << "Yes";
    }
    else
    {
        cout << "No";
    }
    return 0;
}

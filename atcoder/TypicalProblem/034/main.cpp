#include <atcoder/all>
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <unordered_set>

using namespace atcoder;
using namespace std;
using ll = long long;

int main()
{
    ll N, K;
    cin >> N >> K;
    vector<ll> A(N);
    for (ll i = 0; i < N; i++)
    {
        cin >> A[i];
    }
    map<ll, ll> memo;
    ll ans = 0;
    ll right = 0;
    ll cnt = 0;
    for (ll i = 0; i < N; i++)
    {
        while (right < N)
        {
            if (memo[A[right]] == 0 && cnt == K)
            {
                break;
            }
            if (memo[A[right]] == 0)
            {
                cnt += 1;
            }
            memo[A[right]] += 1;
            right += 1;
        }
        ans = max(ans, right - i);
        if (memo[A[i]] == 1)
        {
            cnt -= 1;
        }
        memo[A[i]] -= 1;
    }
    cout << ans << endl;
    return 0;
}

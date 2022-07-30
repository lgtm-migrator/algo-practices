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
    ll L, R;
    cin >> L >> R;
    ll ans = 0;
    for (ll diff = R - L; diff > 0; diff--)
    {
        ll start = L;
        ll end = R;
        while (start + diff <= R || end - diff >= L)
        {
            if (start == end)
            {
                cout << 1;
                return 0;
            }
            ll numR = start + diff;
            if (numR <= R && gcd(numR, start) == 1)
            {
                // cout << start << numR << endl;
                cout << diff;
                return 0;
            }
            ll numL = end - diff;
            if (numL >= L && gcd(numL, end) == 1)
            {
                // cout << numL << end << endl;
                cout << diff;
                return 0;
            }
            if (start + diff <= R)
            {
                start += 1;
            }
            else
            {
                end -= 1;
            }
        }
    }
    return 0;
}

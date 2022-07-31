#include <atcoder/all>
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <cmath>

using namespace atcoder;
using namespace std;
using ll = long long;

int main()
{
    ll a, b, c;
    cin >> a >> b >> c;
    ll right = c;
    for (ll i = 1; i < b; i++)
    {
        right *= c;
    }
    bool yes = a < right;
    if (yes)
    {
        cout << "Yes";
    }
    else
    {
        cout << "No";
    }
    return 0;
}

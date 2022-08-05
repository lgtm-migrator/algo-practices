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
    ll A, B;
    cin >> A >> B;
    ll D = gcd(A, B);
    // 10 ** 18はdoubleだとオーバーフローする
    // lcm = A * B / D >= pow(10, 18);
    // lcm / A == B / D >= pow(10, 18) / A;
    ll pow_10_18 = 1;
    for (ll i = 0; i < 18; i++)
    {
        pow_10_18 *= 10;
    }

    if (B / D > pow_10_18 / A)
    {
        cout << "Large" << endl;
    }
    else
    {
        cout << A * (B / D) << endl;
    }
    return 0;
}

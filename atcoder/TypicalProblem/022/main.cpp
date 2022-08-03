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
    ll A, B, C;
    cin >> A >> B >> C;
    ll length = gcd(C, gcd(A, B));
    ll ans = 0;
    ans += A / length - 1;
    ans += B / length - 1;
    ans += C / length - 1;
    cout << ans << endl;
    return 0;
}

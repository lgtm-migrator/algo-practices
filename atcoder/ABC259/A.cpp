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
    ll N, M, X, T, D;
    cin >> N >> M >> X >> T >> D;
    cout << T - max(0LL, X - M) * D << endl;
    return 0;
}

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
    ll N, A, B;
    cin >> N >> A >> B;
    ll cnt = A - 1;
    if (B >= A)
    {
        cout << N - A;
        return 0;
    }
    // A > B and n > A and N % A < B
    ll times = N / A - 1;
    if ((A + N % A) % A < B)
    {
        cnt += times;
    }
    cout << N - cnt;
    return 0;
}

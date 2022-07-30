#include <atcoder/all>
#include <iostream>
#include <vector>

using namespace atcoder;
using namespace std;

int main()
{
    int L1, R1, L2, R2;
    cin >> L1 >> R1 >> L2 >> R2;
    int L = max(L1, L2);
    int R = min(R1, R2);
    cout << max(0, (R - L));
    return 0;
}
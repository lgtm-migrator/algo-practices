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
    ll N;
    cin >> N;
    vector<string> S(N);
    for (ll i = 0; i < N; i++)
    {
        cin >> S[i];
    }
    unordered_set<string> kinds;
    for (ll i = 0; i < S.size(); i++)
    {
        string si = S[i];
        if (kinds.count(si) == 0)
        {
            kinds.insert(si);
            cout << i + 1 << endl;
        }
    }
    return 0;
}

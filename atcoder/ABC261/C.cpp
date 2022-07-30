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
    ll N;
    cin >> N;
    map<string, ll> counter = {};
    for (ll i = 0; i < N; i++)
    {
        string line;
        cin >> line;
        ll cnt = 0;
        if (counter.find(line) != counter.end())
        {
            cnt = counter[line];
        }
        if (cnt >= 1)
        {
            cout << line << "(" << to_string(cnt) << ")" << endl;
        }
        else
        {
            cout << line << endl;
        }
        counter[line] = cnt + 1;
    }
    return 0;
}
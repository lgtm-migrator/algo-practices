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
    string S;
    cin >> N;
    cin >> S;
    if (S == "BA")
    {
        cout << "No" << endl;
        return 0;
    }
    if (S[0] == 'A' && S[S.size() - 1] == 'B')
    {
        cout << "No" << endl;
        return 0;
    }
    cout << "Yes" << endl;
    return 0;
}

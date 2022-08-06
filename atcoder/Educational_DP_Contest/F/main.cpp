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
    string S, T;
    cin >> S;
    cin >> T;
    vector<vector<string>> dp(S.size() + 1, vector<string>(T.size() + 1, "1"));
    dp[0][0] = "";
    ll i = 1, j = 1;
    while (i < S.size() || j < T.size())
    {
        i = min(i, ll(S.size()) - 1);
        j = min(j, ll(T.size()) - 1);
        cout << "i:" << i << "j:" << j << endl;
        // 選ばない場合
        if (dp[i][j] == "1")
        {
            dp[i][j] = dp[i - 1][j - 1];
        }
        else if (dp[i][j].size() < dp[i - 1][j - 1].size())
        {
            dp[i][j] = dp[i - 1][j - 1];
        }
        // Sが選べる場合
        if (S.size() > i && dp[i - 1][j] != "1")
        {
            if (dp[i][j] == "1")
            {
                dp[i][j] = dp[i - 1][j] + S[i];
            }
            else if (dp[i][j].size() <= dp[i - 1][j].size())
            {
                dp[i][j] = dp[i - 1][j] + S[i];
            }
        }
        // Tが選べる場合
        if (T.size() > j && dp[i][j - 1] != "1")
        {
            if (dp[i][j] == "1")
            {
                dp[i][j] = dp[i][j - 1] + T[j];
            }
            else if (dp[i][j].size() <= dp[i][j - 1].size())
            {
                dp[i][j] = dp[i][j - 1] + T[j];
            }
        }
        i++;
        j++;
    }
    cout << dp[S.size() - 1][T.size() - 1] << endl;
    return 0;
}

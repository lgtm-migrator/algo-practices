#include <iostream>
#include <string>
#include <vector>

using namespace std;

template <class T>
void chmin(T &a, T b)
{
    if (a > b)
    {
        a = b;
    }
}

const int INF = 1 << 29; // 十分大きな値 (2^29)

int main()
{
    // input
    string S, T;
    cin >> S >> T;

    // DPテーブル定義
    vector<vector<int>> dp(S.size() + 1, vector<int>(T.size() + 1, INF));

    // DP初期条件
    dp[0][0] = 0;

    // DPループ
    for (int i = 0; i <= S.size(); i++)
    {
        for (int j = 0; j <= T.size(); j++)
        {
            // 変更操作
            if (i > 0 && j > 0)
            {
                if (S[i - 1] == T[j - 1])
                {
                    // 特定の位置に関して同じ文字なので、移動するコストは発生しない
                    chmin(dp[i][j], dp[i - 1][j - 1]);
                }
                else
                {
                    // 文字を入れ替える場合は両方の単語で一つ前の状態からコストが1増える
                    chmin(dp[i][j], dp[i - 1][j - 1] + 1);
                }
            }

            // 削除処理（Sから1文字削除する）
            if (i > 0)
            {
                chmin(dp[i][j], dp[i - 1][j] + 1);
            }

            // 追加処理（Sに1文字追加する→Tから1文字削除する）
            if (j > 0)
            {
                chmin(dp[i][j], dp[i][j - 1] + 1);
            }
        }
    }

    int result = dp[S.size()][T.size()];
    cout << result << endl;
    return 0;
}
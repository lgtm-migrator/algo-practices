#include <iostream>
#include <vector>

using namespace std;

template <class T>
void chmax(T &a, T b)
{
    if (a < b)
    {
        a = b;
    }
}

// 動的計画法
// 一つ前の状態が確定で決まっているときに現在の値を更新して緩和処理を進める
int main()
{
    // 変数の定義
    int N;
    long long W;
    cin >> N >> W;
    vector<long long> weight(N), value(N);

    // 入力
    for (int i = 0; i < N; i++)
    {
        // 一つ目の入力をweightへ、二つ目の入力をvaluesへ
        cin >> weight[i] >> value[i];
    }

    // DPテーブル
    vector<vector<long long>> dp(N + 1, vector<long long>(W + 1, 0));

    // Loop
    for (int i = 0; i < N; ++i)
    {
        for (int w = 0; w <= W; ++w)
        {
            // i番目の品物を選ぶ場合
            // w - weight[i]以上の空き容量があるかどうか
            if (weight[i] <= w)
            {
                // i番目の品物を選ぶ場合（選ぶことが容量的にできるので、選んで価値を大きくする）
                // 配る遷移
                chmax(dp[i + 1][w], dp[i][w - weight[i]] + value[i]);
            }
            else
            {
                // i番目の品物を選ばない場合
                chmax(dp[i + 1][w], dp[i][w]);
            }
        }
    }
    cout << dp[N][W] << endl;
    return 0;
}
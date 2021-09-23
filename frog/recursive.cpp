#include <iostream>
#include <vector>

using namespace std;

template<class T>void chmin(T& a, T b) {
    a = min(a, b);
}

const long long INF = 1LL << 60;

// 入力データ
int N;
vector<long long> h;
// メモ用のDPテーブル
vector<long long> dp;

long long rec(int i) {
    // dpの値が既に計算されていたら、そのまま結果を返す
    if (dp[i] < INF) return dp[i];

    // ベースケースベースケース
    if ( i == 0 ) return 0;
    // 答えの値を格納する変数
    long long res = INF;
    
    // i - 1から来た場合
    chmin(res, rec(i-1) + abs(h[i] - h[i-1]));

    // i - 2から来た場合（i > 1のみ）
    if (i > 1) chmin(res, rec(i-2) + abs(h[i] - h[i-2]));

    dp[i] = res;

    return res;
}


int main() {
    cin >> N;

    h.resize(N);
    for (int i = 0; i < N; ++i) {
        cin >> h[i];
    }

    // 初期条件の設定。最悪の条件にしておく
    dp.assign(N, INF);

    cout << rec(N-1) << endl;
    return 0;
}
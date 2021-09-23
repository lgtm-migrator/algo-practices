#include <iostream>
#include <vector>

using namespace std;

const long long INF = 1LL << 60; // 2^60

int main() {
    int N;
    cin >> N;
    vector<long long> h(N);
    for (int i = 0; i < N; ++i) {
        cin >> h[i];
    }
    // 配列dpを定義
    // 初期値は無限大（最悪の条件）に設定しておく
    vector<long long> dp(N, INF);

    // 初期条件
    dp[0] = 0;

    // ループ
    for (int i = 0; i < N; ++i) {
        if (i == 1) {
            dp[i] = abs(h[i] - h[i-1]);
        } else {
            dp[i] = min(dp[i-1] + abs(h[i] - h[i-1]), dp[i-2] + abs(h[i] - h[i-2]));
        }
    }

    // 答え
    cout << dp[N-1] << endl;

    return 0;
}
#include <iostream>
#include <vector>
#include <tuple>

using namespace std;

int main() {	
	int N;
	cin >> N;
	vector<tuple<int, int, int>> actions(N, { 0, 0, 0 });
	for (int i = 0; i < N; i++) {
		int a, b, c;
		cin >> a >> b >> c;
		actions[i] = {a, b, c};
	}
	// 配る遷移
	vector<tuple<int, int, int>> dp(N, {0, 0, 0});
	for (int i = 0; i < N; i++) {
		auto [a, b, c] = actions[i];				
		if (i == 0) {
			dp[0] = {a, b, c};
		} else {
			auto prev = dp[i-1];
			dp[i] = {
				max(get<1>(prev) + a, get<2>(prev) + a),
				max(get<0>(prev) + b, get<2>(prev) + b),
				max(get<0>(prev) + c, get<1>(prev) + c),
			};
		}
	}
	cout << max(get<0>(dp[N-1]), max(get<1>(dp[N-1]), get<2>(dp[N-1]))) << endl;
	return 0;
}
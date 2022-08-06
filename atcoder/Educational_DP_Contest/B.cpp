#include <iostream>
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

int main()
{
    // read
    int N, K;
    long long inf = 1LL << 20;
    cin >> N >> K;
    vector<int> costs(N);
    for (int i = 0; i < N; i++)
    {
        cin >> costs[i];
    }
    // calc
    vector<long long> dp(N, inf);
    dp[0] = 0;
    for (int i = 0; i < N; i++)
    {
        for (int k = 1; k <= K; k++)
        {
            if (i - k >= 0)
            {
                chmin(dp[i], dp[i - k] + abs(costs[i] - costs[i - k]));
            }
        }
    }
    cout << dp[N - 1] << endl;
    return 0;
}
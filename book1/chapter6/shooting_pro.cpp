#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

const long long INF = 1e+12;

int main()
{
    int N;
    cin >> N;
    vector<long long> h(N), s(N);
    for (int i = 0; i < N; i++)
    {
        cin >> h[i] >> s[i];
    }
    // 2分探索
    long long left = 0, right = INF;
    while (right - left > 1)
    {
        long long mid = (right + left) / 2;

        bool ok = true;
        vector<long long> time_vec(N, 0);
        for (int i = 0; i < N; i++)
        {
            // そもそも風船を割ることができる高さ（初期値:h[s]）にmidがいるかどうか
            if (mid < h[i])
            {
                ok = false;
            }
            else
            {
                time_vec[i] = (mid - h[i]) / s[i];
            }
            // 時間制限順にソート
            sort(time_vec.begin(), time_vec.end());
            // 時間制限が差し迫っている順に割る
            for (int i; i < N; i++)
            {
                const int time_cost_per_shoot = 1;
                const int need_time = i * time_cost_per_shoot;
                if (time_vec[i] < need_time)
                {
                    ok = false;
                }
            }
        }
        if (ok)
        {
            right = mid;
        }
        else
        {
            left = mid;
        }
    }
    cout << right << endl;
    return 0;
}
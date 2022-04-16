#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int N, K;
    cin >> N >> K;
    vector<int> a(N), b(N);
    for (int i = 0; i < N; i++)
    {
        cin >> a[i];
    }
    for (int i = 0; i < N; i++)
    {
        cin >> b[i];
    }

    // bをソート
    sort(b.begin(), b.end());

    int minimum = 1e+8;

    for (int i = 0; i < N; i++)
    {
        // aの要素を固定
        auto it = lower_bound(b.begin(), b.end(), K - a[i]);
        int val = *it;
        int sum = a[i] + val;

        if (minimum > sum)
        {
            minimum = sum;
        }
    }

    cout << minimum << endl;

    return 0;
}
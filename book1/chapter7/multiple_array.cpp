#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    // 入力
    int N;
    cin >> N;
    vector<long long> A(N), B(N);
    for (int i = 0; i < N; ++i)
    {
        cin >> A[i] >> B[i];
    }

    long long ret = 0;
    // 計算
    for (int i = N - 1; i >= 0; --i)
    {
        long long remain = A[i] % B[i];
        if (remain == 0)
        {
            continue;
        }
        long long diff = B[i] - remain;
        ret += diff;
        for (int j = 0; j <= i; j++)
        {
            A[j] += diff;
        }
    }
    cout << ret << endl;
    return 0;
}
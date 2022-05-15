// Link: https://algo-method.com/tasks/307
#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int N;
    cin >> N;
    vector<int> nums(N);
    for (int i = 0; i < N; i++)
    {
        cin >> nums[i];
    }
    int dp = max(0, nums[0]);
    for (int i = 1; i < N; i++)
    {
        int num = nums[i];
        if (dp < dp + num)
        {
            dp = dp + num;
        }
    }
    cout << dp << endl;
    return 0;
}
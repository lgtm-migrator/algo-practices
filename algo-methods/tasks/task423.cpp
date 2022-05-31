#include <iostream>
#include <vector>

using namespace std;

long long func(long long n, vector<long long> &nums)
{
    if (nums[n] != -1)
    {
        return nums[n];
    }
    nums[n] = func(n - 1, nums) + func(n - 2, nums);
    return nums[n];
}

int main()
{
    long long N;
    cin >> N;
    vector<long long> nums(N + 1);
    nums.assign(N + 1, -1);
    nums[0] = 0;
    nums[1] = 1;
    func(N, nums);
    cout << nums[N] << endl;
    return 0;
}
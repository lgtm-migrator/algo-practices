#include <iostream>

using namespace std;

bool Condition(int x)
{
    // 11~100の範囲で5で割り切れる数字を探す
    return x > 10 && x % 5 == 0;
}

// TOOD: Conditionを満たす最小値を取得できるようにする
int BinarySearch(int initial_l, int initial_r)
{
    int left = initial_l;
    int right = initial_r;

    // rightはleftを追い越さない
    // rightは常にConditionがtrueを返す最小値
    // leftは常にConditionがfalseを返す最大値
    while (right > left + 1)
    {
        int mid = left + (right - left) / 2;
        if (Condition(mid))
        {
            right = mid;
        }
        else
        {
            left = mid;
        }
    }
    return right;
}

int main()
{
    cout << BinarySearch(10, 40) << endl;
}
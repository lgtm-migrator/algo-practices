#include <iostream>
#include <vector>

using namespace std;

int main()
{
    vector<int> a = {
        4,
        3,
        5,
        6,
        43,
        13,
        46,
        78,
        242,
    };
    // 0番目の要素を出力（O(1)）
    cout << a[0] << endl;
    // 2番目の要素を5に置き換える（O(1)）
    a[2] = 5;
    // 2番目の要素を出力（O(1)）
    cout << a[2] << endl;
    return 0;
}
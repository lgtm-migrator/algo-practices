#include <iostream>
#include <vector>

using namespace std;

// return index of searched value.
int BinarySearch(vector<int> a, int a_size, int key)
{
    int left = 0;
    int right = a_size - 1;
    while (right >= left)
    {
        int mid = (left + right) / 2;
        int value = a[mid];
        if (key == value)
        {
            return mid;
        }
        else if (key > value)
        {
            left = mid + 1;
        }
        else if (key < value)
        {
            right = mid - 1;
        }
    }
    return -1;
}

int main()
{
    const vector<int> a = {
        3,
        5,
        8,
        10,
        14,
        17,
        21,
        39,
    };
    const int a_size = a.size();
    cout << BinarySearch(a, a_size, 10) << endl;
    cout << BinarySearch(a, a_size, 3) << endl;
    cout << BinarySearch(a, a_size, 39) << endl;

    cout << BinarySearch(a, a_size, -100) << endl;
    cout << BinarySearch(a, a_size, 9) << endl;
    cout << BinarySearch(a, a_size, 100) << endl;
}
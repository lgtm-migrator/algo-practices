#include "iostream"

using namespace std;

int main()
{
    int left = 20;
    int right = 36;

    while (right - left > 1)
    {
        int mid = (right + left) / 2;

        cout << "Is age bigger than " << mid << "? (yes / no)" << endl;
        string ans;
        cin >> ans;
        if (ans == "yes")
        {
            left = mid;
        }
        else
        {
            right = mid;
        }
    }

    cout << "The age is " << right << "!" << endl;

    return 0;
}
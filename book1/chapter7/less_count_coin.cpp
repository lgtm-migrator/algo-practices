#include <iostream>
#include <vector>

using namespace std;

const vector<int> kinds = {500, 100, 50, 10, 5, 1};

int main()
{
    int price;
    cin >> price;
    vector<int> having(6);
    for (int i = 0; i < 6; i++)
    {
        cin >> having[i];
    }
    int ret = 0;
    for (int i = 0; i < 6; i++)
    {
        int count = price / kinds[i];
        if (count > having[i])
        {
            count = having[i];
        }
        price -= count * kinds[i];
        ret += count;
    }
    cout << ret << endl;
    return 0;
}
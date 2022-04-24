#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

using District = pair<int, int>;

bool compare(const District &lhs, const District &rhs)
{
    return lhs.second < rhs.second;
}

int main()
{
    int N;
    cin >> N;
    vector<District> districts(N);
    vector<District> result;
    for (int i = 0; i < N; i++)
    {
        cin >> districts[i].first >> districts[i].second;
    }
    sort(districts.begin(), districts.end(), compare);
    int current_second_time = 0;
    for (int i = 0; i < N; i++)
    {
        if (current_second_time > districts[i].first)
        {
            continue;
        }
        result.push_back(districts[i]);
        current_second_time = districts[i].second;
    }
    cout << result.size() << endl;
    return 0;
}
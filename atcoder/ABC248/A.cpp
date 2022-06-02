#include <iostream>

using namespace std;

int main()
{
    string S;
    cin >> S;
    int sum = 45;
    for (int i = 0; i < S.size(); i++)
    {
        int c = int(S[i] - '0');
        sum -= c;
    }
    cout << sum << endl;
    return 0;
}

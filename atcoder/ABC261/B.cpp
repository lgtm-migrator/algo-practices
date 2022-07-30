#include <atcoder/all>
#include <iostream>
#include <vector>
#include <map>

using namespace atcoder;
using namespace std;

vector<vector<char>> table;

int main()
{
    int N;
    cin >> N;
    map<char, char> mapping = {
        {'W', 'L'},
        {'D', 'D'},
        {'L', 'W'},
    };
    table.assign(N, vector<char>(N));
    for (int i = 0; i < N; i++)
    {
        string line;
        cin >> line;
        for (int j = 0; j < line.length(); j++)
        {
            const char c = line[j];
            table[i][j] = c;
        }
    }
    for (int i = 0; i < N; i++)
    {
        for (int j = i; j < N; j++)
        {
            if (i == j)
            {
                continue;
            }
            int symmetryX, symmetryY;
            symmetryX = i;
            symmetryY = j;
            if (table[symmetryY][symmetryX] != mapping[table[i][j]])
            {
                cout << "incorrect";
                return 0;
            }
        }
    }
    cout << "correct";
    return 0;
}
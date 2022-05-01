#include <iostream>
#include <vector>

using namespace std;

using Graph = vector<vector<int>>;

int main()
{
    int N, M;
    cin >> N >> M;
    Graph graph(N);
    for (int i = 0; i < M; i++)
    {
        int a, b;
        cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }
    return 0;
}
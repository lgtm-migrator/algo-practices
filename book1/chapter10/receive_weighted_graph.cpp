#include <iostream>
#include <vector>

using namespace std;

struct Edge
{
    int to;
    long long w;
    Edge(int to, long long w) : to(to), w(w) {}
};

using Graph = vector<vector<Edge>>;

int main()
{
    int N, M;
    cin >> N >> M;
    Graph graph(N);
    for (int i = 0; i < M; i++)
    {
        int a, b, w;
        cin >> a >> b >> w;
        graph[a].push_back(Edge(b, w));
    }
    return 0;
}
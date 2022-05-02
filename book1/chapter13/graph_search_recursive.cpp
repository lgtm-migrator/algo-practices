#include <iostream>
#include <vector>

using namespace std;

using Graph = vector<vector<int>>;

vector<bool> seen;

void dfs(const Graph &graph, int v)
{
    seen[v] = true;

    for (auto x : graph[v])
    {
        if (seen[x])
            continue;
        dfs(graph, x);
    }
}

int main()
{
    int V, E;
    cin >> V >> E;
    Graph graph(V);
    for (int i = 0; i < E; i++)
    {
        int a, b;
        cin >> a >> b;
        // 有向グラフ
        graph[a].push_back(b);
    }
    // 探索
    seen.assign(V, false);
    for (int v = 0; v < V; v++)
    {
        if (seen[v])
            continue;
        dfs(graph, v);
    }
    return 0;
}
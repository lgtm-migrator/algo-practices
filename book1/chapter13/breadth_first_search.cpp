#include <iostream>
#include <vector>
#include <queue>

using namespace std;

using Graph = vector<vector<int>>;

// 頂点sから各頂点への最短経路を返却
vector<int> BFS(Graph &G, int s)
{
    const int size = G.size();
    // index: vにおける最短経路が格納されている
    vector<int> dist(size, -1);
    // 橙色のvertex
    queue<int> que;

    // 初期設定
    dist[0] = 0;
    que.push(0); // 0を橙色にする

    while (!que.empty())
    {
        int v = que.front();
        que.pop();
        for (int next_v : G[v])
        {
            if (dist[next_v] != -1)
                continue;
            dist[next_v] = dist[v] + 1;
            que.push(next_v);
        }
    }
    return dist;
}

int main()
{
    int V, E;
    cin >> V >> E;

    // 無向グラフ
    Graph graph(V);
    for (int i = 0; i < E; i++)
    {
        int a, b;
        cin >> a >> b;
        // a→bの経路を追加
        graph[a].push_back(b);
        // b→aの経路を追加
        graph[b].push_back(a);
    }

    // 頂点0を始点としたBFS
    vector<int> bfs = BFS(graph, 0);

    // 結果出力
    for (int i = 0; i < V; i++)
    {
        cout << i << ": " << bfs[i] << endl;
    }
    return 0;
}
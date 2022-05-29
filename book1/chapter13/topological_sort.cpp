// トポロジカルソート:
// 深さ優先探索における再帰関数を抜けた順序に頂点を並べ、
// それを逆順に並べ直すことでトポロジカルソートを得ることができる

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
using Graph = vector<vector<int>>;

vector<int> order;
vector<bool> seen;
void dfs(Graph &G, int v)
{
    seen[v] = true;

    for (auto next_vertex : G[v])
    {
        if (seen[next_vertex])
            continue;
        dfs(G, next_vertex);
    }

    // 帰りかけ順
    order.push_back(v);
}

int main()
{
    int N, M;
    cin >> N >> M;
    Graph G(N);
    for (int i = 0; i < M; i++)
    {
        int a, b;
        cin >> a >> b;
        G[a].push_back(b);
    }
    seen.assign(N, false);
    order.clear();

    for (int i = 0; i < N; i++)
    {
        if (seen[i])
            continue;
        dfs(G, i);
    }
    reverse(order.begin(), order.end());

    for (auto v : order)
    {
        cout << v << " -> ";
    }
    cout << endl;
}
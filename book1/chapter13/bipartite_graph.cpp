// 二部グラフ...白黒の頂点同士が隣接することはなく、黒色の頂点同士が隣接することもない

// 二部グラフの解法
// Gが連結ではない場合、全ての連結成分が二部グラフであるかどうかを判定すれば良い

#include <iostream>
#include <vector>

using namespace std;
using Graph = vector<vector<int>>;

vector<int> color;
bool dfs(const Graph &G, int v, int cur = 0)
{
    color[v] = cur;

    // 次の処理
    for (auto next_v : G[v])
    {
        if (color[next_v] != -1)
        {
            if (color[next_v] == cur)
                return false;

            continue;
        }
        bool adujacent_color = dfs(G, next_v, 1 - cur);
        if (!adujacent_color)
        {
            return false;
        }
    }
    return true;
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
        G[b].push_back(a);
    }

    color.assign(N, -1);
    bool is_bipartite = true;
    for (int v = 0; v < N; v++)
    {
        if (color[v] != -1)
            continue;
        if (!dfs(G, v))
            is_bipartite = false;
    }
    if (is_bipartite)
    {
        cout << "Yes" << endl;
    }
    else
    {
        cout << "No" << endl;
    }
}
#include <iostream>
#include <vector>
#include <stack>

using namespace std;

using Graph = vector<vector<int>>;

void search(const Graph &G, int s)
{
    int N = (int)G.size();

    vector<bool> seen(N, false);

    // 深さ優先探索
    stack<int> todo;

    seen[s] = true;
    todo.push(s);

    // todoが空になるまで探索を行う
    while (!todo.empty())
    {
        int v = todo.top();
        todo.pop();
        // vから辿れる頂点を全て調べる
        for (int x : G[v])
        {
            // 既に発見済みであればスキップ
            if (seen[x])
            {
                continue;
            }
            // 新たな頂点の発見
            seen[x] = true; // サイクルを含むグラフの場合、これがないと無限ループ
            todo.push(x);
        }
    }
}
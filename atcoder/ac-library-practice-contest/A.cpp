#include <atcoder/all>
#include <iostream>
#include <vector>

using namespace std;
using namespace atcoder;
using Graph = vector<vector<int>>;

int main()
{
    int N, Q;
    cin >> N >> Q;
    dsu d(N);

    for (int i = 0; i < Q; i++)
    {
        int t, u, v;
        cin >> t >> u >> v;
        if (t == 0)
        {
            d.merge(u, v);
        }
        else
        {
            bool isSame = d.same(u, v);
            if (isSame)
            {
                cout << 1 << endl;
            }
            else
            {
                cout << 0 << endl;
            }
        }
    }
}
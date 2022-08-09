#include <atcoder/all>
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>

using namespace atcoder;
using namespace std;
using ll = long long;

const ll INF = 1LL << 60;

struct State
{
    ll r;
    ll c;
    ll dir;
};

const vector<ll> drs = {0, 1, 0, -1};
const vector<ll> dcs = {1, 0, -1, 0};

int main()
{
    ll H, W, rs, cs, rt, ct;
    cin >> H >> W;
    cin >> rs >> cs;
    cin >> rt >> ct;
    rs--;
    cs--;
    rt--;
    ct--;
    vector<string> S(H);
    for (ll i = 0; i < H; i++)
    {
        cin >> S[i];
    }
    vector<vector<vector<ll>>> dist(H, vector(W, vector(4, INF)));
    deque<State> que;
    for (ll i = 0; i < 4; i++)
    {
        dist[rs][cs][i] = 0;
        que.push_back({rs, cs, i});
    }
    while (!que.empty())
    {
        State front = que.front();
        que.pop_front();
        for (ll i = 0; i < 4; i++)
        {
            ll nr = front.r + drs[i];
            ll nc = front.c + dcs[i];
            if (0LL > nr || H <= nr || 0LL > nc || W <= nc)
            {
                continue;
            }
            if (S[nr][nc] == '#')
            {
                continue;
            }
            ll cost;
            if (i == front.dir)
            {
                cost = 0;
            }
            else
            {
                cost = 1;
            }
            if (dist[front.r][front.c][front.dir] + cost >= dist[nr][nc][i])
            {
                continue;
            }
            if (i == front.dir)
            {
                que.push_front({nr, nc, i});
            }
            else
            {
                que.push_back({nr, nc, i});
            }
            dist[nr][nc][i] = dist[front.r][front.c][front.dir] + cost;
        }
    }
    ll ans = INF;
    for (ll i = 0; i < 4; i++)
    {
        ans = min(ans, dist[rt][ct][i]);
    }
    cout << ans << endl;
    return 0;
}

#include <iostream>
#include <vector>
#include <set>

using ll = long long;
constexpr ll INF64 = (1LL << 62) - 1;

using namespace std;

multiset<ll> sets;

void ope1(ll x)
{
    sets.insert(x);
}

void ope2(ll x, int k)
{
    // sets多重集合の内、xより大きい最小の数字のポインタイテレータ
    auto begin = sets.upper_bound(x);
    bool exists = true;
    // beginをk個先まで進める
    // その時の値を出力する
    for (int i = 0; i < k; i++)
    {
        if (begin == sets.begin())
        {
            exists = false;
            break;
        }
        begin--;
    }
    if (exists)
    {
        cout << *begin << endl;
    }
    else
    {
        cout << -1 << endl;
    }
}

void ope3(ll x, int k)
{
    // sets内のx以上の数字の内で最も小さいもののポインタイテレータ
    auto cur = sets.lower_bound(x);
    bool exists = true;
    for (int i = 0; i < k - 1; i++)
    {
        if (cur == sets.end())
        {
            exists = false;
            break;
        }
        cur++;
    }
    if (exists && cur != sets.end())
    {
        cout << *cur << endl;
    }
    else
    {
        cout << -1 << endl;
    }
}

int main()
{
    ll Q;
    cin >> Q;
    vector<vector<ll>> commands(Q, vector<ll>(3));
    for (ll i = 0; i < Q; i++)
    {
        int command;
        cin >> command;
        if (command == 1)
        {
            ll x;
            cin >> x;
            commands[i] = {command, x};
        }
        else if (command == 2 || command == 3)
        {
            ll x, k;
            cin >> x >> k;
            commands[i] = {command, x, k};
        }
    }

    for (vector<ll> command : commands)
    {
        if (command[0] == 1)
        {
            ope1(command[1]);
        }
        else if (command[0] == 2)
        {
            ope2(command[1], command[2]);
        }
        else if (command[0] == 3)
        {
            ope3(command[1], command[2]);
        }
    }
    return 0;
}

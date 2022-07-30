#include <iostream>
#include <vector>

using namespace std;

struct Block
{
    int x;
    int y;
    char c;

    bool can_enter()
    {
        return c != '#';
    }
};

using Graph = vector<vector<Block>>;

vector<vector<bool>> seen;
vector<vector<Block>> fields;

vector<int> dxs{1, -1, 0, 0};
vector<int> dys{0, 0, -1, 1};

Block sb;
Block gb;

void dfs(const Block &edge, int H, int W)
{
    seen[edge.y][edge.x] = true;
    for (int i = 0; i < 4; i++)
    {
        int nx = edge.x + dxs[i];
        int ny = edge.y + dys[i];
        if (nx < 0 || nx >= W || ny < 0 || ny >= H)
        {
            continue;
        }
        if (!fields[edge.y][edge.x].can_enter())
        {
            continue;
        }
        if (seen[ny][nx])
        {
            continue;
        }
        Block nxt = fields[ny][nx];
        dfs(nxt, H, W);
    }
}

int main()
{
    int H, W;
    cin >> H >> W;
    fields.assign(H, vector<Block>(W));
    seen.assign(H, vector<bool>(W, false));
    for (int i = 0; i < H; i++)
    {
        string line;
        cin >> line;
        for (int j = 0; j < line.length(); j++)
        {
            Block block{j, i, line[j]};
            if (block.c == 's')
            {
                sb = block;
            }
            else if (block.c == 'g')
            {
                gb = block;
            }
            fields[i][j] = block;
        }
    }
    dfs(sb, H, W);
    if (seen[gb.y][gb.x])
    {
        cout << "Yes";
    }
    else
    {
        cout << "No";
    }

    return 0;
}
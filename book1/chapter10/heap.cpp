#include <iostream>
#include <vector>

using namespace std;

struct Heap
{
    vector<int> heap;

    Heap() {}

    void push(int x)
    {
        heap.push_back(x);
        // 挿入された頂点のindex番号
        int i = int(heap.size()) - 1;
        while (i > 0)
        {
            int parent = (i - 1) / 2;
            if (heap[parent] >= x)
                break;
            heap[i] = heap[parent];
            heap[parent] = x;
            i = parent;
        }
    }

    // 最大値を取得
    int root()
    {
        if (heap.empty())
            return -1;
        else
            return heap[0];
    }

    // 最大値を削除
    void pop()
    {
        if (heap.empty())
            return;
        // 頂点に持ってくる値（一番最後の要素）
        int x = heap.back();
        // 最後の値を削除
        heap.pop_back();
        int i = 0;
        // 子が最後の要素ではない限り
        while (i * 2 + 1 < (int)heap.size())
        {
            // 子頂点同士を比較して大きい方をchild1とする
            int child1 = i * 2 + 1, child2 = i * 2 + 2;
            if (child2 < int(heap.size()) && heap[child1] < heap[child2])
            {
                child1 = child2;
            }
            if (child1 <= x)
                break;
            heap[i] = heap[child1];
            i = child1;
        }
        heap[i] = x;
    }
};

int main()
{
    Heap h;
    h.push(5);
    h.push(3);
    h.push(7);
    h.push(1);
    cout << h.root() << endl;
    h.pop();
    cout << h.root() << endl;
    h.push(11);
    cout << h.root() << endl;
    return 0;
}